import sys
import nltk
from nltk.chat.util import Chat, reflections


class Chat(Chat):
    def respond(self, message):
        # Call the respond method of the parent class
        response = super().respond(message)
        
         # Check if the response is None
        if response is None:
            return "I'm sorry, I don't understand. Please ask me something else."
        
        return response

# Define the chatbot's responses 
pairs = [
    ['(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hi, how can I assist you today?']],
    ['(.*) your name?',['My name is HR Bot.']],
    ['(what is your name|what are you called)', ['My name is HR Bot.']],
    ['(How are you?)',['Good what is your question?']],
    ['(what do you do|what is your purpose)', ['I am here to help with any HR-related questions you have.']],
    ['(employee benefits|benefits|insurance)', ['We offer a variety of benefits to our employees, including health insurance and retirement plans.']],
    ['(vacation time|vacation days|pto)', ['Employees receive a certain number of paid time off days per year, which can be used for vacation or personal reasons.']],
    ['(how do I sign up for benefits|benefits enrollment)', ['You can sign up for benefits during the open enrollment period, which typically occurs once a year.']],
    ['(new employee|onboarding|orientation)', ['New employees will receive an orientation to the company, including an overview of company policies and procedures.']],
    ['(What benefits does the company offer?)',['Our company offers a range of benefits including health insurance, retirement plans, paid time off, and professional development opportunities.']],
    ['(How can I apply for a job at your company?)',['You can visit our careers page on our website and search for available positions. Once you find a position you are interested in, you can apply online by submitting your resume and completing our online application.']],
    ['(Can you tell me more about the company culture?)',['Our company values teamwork, innovation, and diversity. We strive to create a welcoming and inclusive workplace where all employees feel valued and respected. We encourage open communication and support employee growth and development.']],
    ['(What is the interview process like at your company?)',['Our interview process typically includes a phone screening, a virtual or in-person interview, and possibly a skills assessment or job-related task. We aim to make the interview process as transparent and comfortable as possible for candidates.']],
    ['(How often do employees receive performance reviews?)',['Our employees typically receive performance reviews on an annual basis. However, managers may also provide feedback and coaching throughout the year to support employee growth and development.']],
    ['(How does the company support employee learning and development?)',['We offer a range of professional development opportunities including workshops, training programs, mentorship, and tuition reimbursement. We encourage employees to take advantage of these opportunities to enhance their skills and knowledge.']],
    ['(What is the companys policy on remote work?)',['Our policy on remote work varies by position and department. Some employees may be eligible for remote work on a part-time or full-time basis, while others may be required to work on-site. Our goal is to provide flexibility while ensuring that employees can effectively perform their job duties.']],
    ['(How does the company handle performance issues or conflicts between employees?)',['We take performance issues and conflicts between employees seriously and aim to resolve them in a fair and respectful manner. Our managers work closely with employees to address concerns and provide support and coaching as needed. In some cases, we may also involve HR or other resources to help resolve the issue.']],
    ['(How does the company promote diversity and inclusion?)',['We are committed to creating a diverse and inclusive workplace and have a range of initiatives to promote diversity and inclusion. These include unconscious bias training for all employees, diversity recruiting efforts, employee resource groups, and a culture of open communication and respect.']],
    ['(Does the company offer any wellness programs for employees?)',['Yes, we offer a variety of wellness programs to support the health and wellbeing of our employees. These include on-site fitness classes, access to mental health resources, and wellness challenges and activities.']],
    ['(What is the companys policy on parental leave?)',['Our parental leave policy varies depending on the employees role and tenure. However, we offer paid parental leave for new parents and encourage employees to take advantage of this benefit.']],
    ['(How does the company handle workplace safety and emergencies?)',['We prioritize workplace safety and have policies and procedures in place to address emergencies and ensure the wellbeing of our employees. These include regular safety training, emergency response plans, and ongoing communication and support.']],
    ['(Does the company offer any employee recognition programs?)',['Yes, we believe in recognizing and celebrating employee achievements and have several recognition programs in place. These include employee awards, spot bonuses, and other forms of recognition for outstanding performance.']],
    ['(How does the company handle requests for accommodations or disabilities?)',['We are committed to providing reasonable accommodations for employees with disabilities and work with employees to determine what accommodations are necessary and appropriate. We also have a process in place for employees to request accommodations and ensure that all requests are handled with confidentiality and respect.']],
    ['(What opportunities are available for advancement within the company?)',['We believe in supporting employee growth and development and offer a range of opportunities for advancement within the company. These may include promotions, lateral moves, and opportunities to take on new projects and responsibilities. We encourage employees to discuss their career goals with their manager and explore available opportunities.']],
    ['(thank you|thanks)', ['You are welcome!']],
    ['(What benefits does the company offer?)',['Our company offers a range of benefits']],
    ['(Okay|Ok)',['Okay If you still have any questions , you can ask me.']],
    ['(Quit|quit)',['Goodbye, Have a nice days']],
    ['(goodbye|bye)', ['Goodbye!', 'Take care!', 'See you later.']]
 ]



# Initialize the chatbot
hr_bot = Chat(pairs, reflections)

# Start the chatbot
hr_bot.converse()

sys.exit(0)