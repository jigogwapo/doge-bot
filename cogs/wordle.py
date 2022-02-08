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
    reduced_answer = list(answer)
    reduced_guess = list(guess)

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
                reduced_answer[i] = " "
                reduced_guess[i] = " "

        for i, letter in enumerate(reduced_guess):
            if letter == " ":
                continue
            elif letter in reduced_answer:
                guess_check_list[i] = 2
                h = reduced_answer.index(letter)
                reduced_answer[h] = " "
        
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
        await ctx.send("Enter your first guess by typing `wordle <guess>`. You can quit any time by typing `wordle quit`")
        print(f'{ctx.author}\'s Wordle game: Correct word is {answer}')
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.startswith("wordle ")

        i = 0
        while i < 6:
            guess = await self.bot.wait_for("message", check=check)

            guessword = guess.content[7:]

            if guessword.lower() == "quit":
                await ctx.send(f'You just quit Wordle. The correct word was {answer}.')
                break

            res = wordle_check(guessword, answer)

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