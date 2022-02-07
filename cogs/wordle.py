import discord
from random import choice
from discord.ext import commands
from helpers.valid_guesses_list import valid_guesses
from helpers.word_list import word_list
from helpers.general_helpers import record_usage

def wordle_check(guess, answer):
    square = {1: "🟩", 2: "🟨", 0: "⬜"}
    guess = guess.lower()
    guess_check_list = [0,0,0,0,0]

    if len(guess) != 5:
        code="error_length"
        message="Please enter a five-letter word."
    elif guess not in valid_guesses:
        code="error_notaword"
        message="That is not a real word."
    else:
        for i, letter in enumerate(guess):
            if letter == answer[i]:
                guess_check_list[i] = 1
            elif letter in answer[i:]:
                guess_check_list[i] = 2
            else:
                guess_check_list[i] = 0
        
        message = " ".join([square[key] for key in guess_check_list])

        if guess_check_list == [1,1,1,1,1]:
            code="correct"
        else:
            code="wrong"

    return {"code": code, "message": message}


class Wordle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.before_invoke(record_usage)
    @commands.group(brief='Play Wordle')
    async def wordle(self, ctx):
        answer = choice(word_list)
        await ctx.send("Enter your first guess.")
        print(f'{ctx.author}\'s Wordle game: Correct word is {answer}')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        i = 0
        while i < 6:
            guess = await self.bot.wait_for("message", check=check)
            if guess.content.lower() == "quit":
                await ctx.send('You just quit Wordle.')
                break
            res = wordle_check(guess.content, answer)
            await ctx.send(res["message"])

            if res["code"] == "correct":
                await ctx.send(f'You got the correct word! ({i+1}/6)')
                break
            elif res["code"].startswith("error"):
                i = i-1
                await ctx.send(f'Please enter another guess. ({i+1}/6)')
            else:
                if i != 5:
                    await ctx.send(f'Please enter another guess. ({i+1}/6)')
                else:
                    await ctx.send(f'You have run out of tries. The correct word was {answer}.')
            i = i+1
        
        print(f'{ctx.author}\'s Wordle game has ended.')


def setup(bot):
    bot.add_cog(Wordle(bot))
    print('Wordle cog successfully added.')