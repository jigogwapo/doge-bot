import random

async def record_usage(self, ctx, *args):
    print(ctx.author, 'used', ctx.command, 'at', ctx.message.created_at)

questions_list = [
    "What is your least favorite chore?",
    "What are three fun facts about yourself?",
    "If you could do anything illegal without getting caught, what would you do?",
    "Would you rather be invisible or have X-ray vision?",
    "What was the last movie you saw?",
    "What’s the most interesting thing you’ve learned at work?",
    "What fun plans do you have for the weekend?",
    "Have you ever been stalked on social media?",
    "How long have you been at your current job?",
    "What’s your favorite word?",
    "If you had a chance to eat dessert for breakfast every day, what dessert would you choose?",
    "What is your favorite book of all time?",
    "What’s the best compliment you’ve ever received?",
    "What’s your favorite city you’ve visited?",
    "Who is your favorite celebrity couple ever?",
    "If you never had to eat one vegetable, which would it be?",
    "If you could live anywhere in the world, where would it be?",
    "If you could be famous, would you want to? Why?",
    "What’s one movie you could watch over and over?",
    "What's the most interesting thing you've read lately?",
    "What makes you most uncomfortable about dating?",
    "What is something you wish you could do everyday?",
    "If you could be a fly on the wall for a C-suite meeting at any company, which company would it be?",
    "What's the most interesting thing you've read lately?",
    "What are your long-term goals?",
    "What's one company perk you'd love to have?",
    "How was your commute here?",
    "Where's your favorite vacation spot?",
    "What’s your all-time favorite band?",
    "What would your ideal life look like?",
    "Do you have any nicknames?",
    "What do you think is a good age to start dating?",
    "If you were to choose one way to be disciplined, what would it be?",
    "If you could have dinner with anyone living or not, who would it be?",
    "If you could publish a book on any subject, what would it be?",
    "What’s the best thing you’ve ever bought off Amazon?",
    "What is your favorite book of all time?",
    "Do you have a signature drink? (Gesture to their glass.)",
    "Do you like to cook?",
    "What is your most embarrassing moment?",
    "What do you think is a good age to start dating?",
    "What’s the weirdest thing you loved as a child?",
    "If we were to raise children, what are the most important things you would want them to learn?",
    "What’s the nicest thing a family member has ever done for you?",
    "Would you want to live on a boat, a mountain or an island?",
    "What does success mean to you?",
    "What instrument would you like to play?",
    "What keeps you up at night?",
    "If you were in a circus, which character would you be?",
    "What is the most memorable lesson you learned from your parents?",
    "What superpower do you wish you could have?",
    "What always makes you laugh, even when you’re upset?",
    "What hurts your feelings?",
    "Would you rather only host fancy dinner parties or theme parties for the rest of your life?",
    "How long have you been at your current job?",
    "Have you ever been on a blind date?",
    "If you could live anywhere in the world, where would it be?"
]

def get_random_question():
    return random.choice(questions_list)
