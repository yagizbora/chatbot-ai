import random
import re

# Define the pairs
pairs = [
    ['(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hi, how can I assist you today?']],
    ['(what is your name|what are you called)', ['My name is HR Bot.']],
    ['(employee benefits|benefits|insurance)', ['We offer a variety of benefits to our employees, including health insurance and retirement plans.']],
    ['(vacation time|vacation days|pto)', ['Employees receive a certain number of paid time off days per year, which can be used for vacation or personal reasons.']]
]

# Test the chatbot with some inputs
inputs = ['hi', 'what are you called', 'what are employee benefits', 'how many vacation days do employees get']
for input in inputs:
    for pattern, responses in pairs:
        if re.search(pattern, input):
            print(random.choice(responses))
            break
