import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
pairs = [
    ['(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hi, how can I assist you today?']],
    ['(what is your name|what are you called)', ['My name is HR Bot.']],
    ['(what do you do|what is your purpose)', ['I am here to help with any HR-related questions you have.']],
    ['(employee benefits|benefits|insurance)', ['We offer a variety of benefits to our employees, including health insurance and retirement plans.']],
    ['(vacation time|vacation days|pto)', ['Employees receive a certain number of paid time off days per year, which can be used for vacation or personal reasons.']],
    ['(how do I sign up for benefits|benefits enrollment)', ['You can sign up for benefits during the open enrollment period, which typically occurs once a year.']],
    ['(new employee|onboarding|orientation)', ['New employees will receive an orientation to the company, including an overview of company policies and procedures.']],
    ['(thank you|thanks)', ['You are welcome!']],
    ['(goodbye|bye)', ['Goodbye!', 'Take care!', 'See you later.']]
]

# Initialize the chatbot
hr_bot = Chat(pairs, reflections)

# Start the chatbot
hr_bot.converse()