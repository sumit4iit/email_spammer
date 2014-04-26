# using Tkinter GUI toolkit
import Tkinter
import smtplib
import os

#GUI class
class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.userName = Tkinter.StringVar()
		self.passWord = Tkinter.StringVar()
		self.victName = Tkinter.StringVar()
		self.count = Tkinter.IntVar()
		self.text = Tkinter.StringVar()

		self.userName.set('email address')		
		self.passWord.set('password')
		self.victName.set('target')
		self.count.set(10)
		self.text.set('This is test message from smtp.python.netsec')
			
		self.userName_label = Tkinter.StringVar()
		self.passWord_label = Tkinter.StringVar()
		self.victName_label = Tkinter.StringVar()
		self.text_label = Tkinter.StringVar()
		self.count_label = Tkinter.StringVar()

		self.userName_label.set('UserName')
		self.passWord_label.set('Password')
		self.victName_label.set('Victim')
		self.count_label.set('Count')
		self.text_label.set('Message')
#label 
#===============================================================================
		label_user = Tkinter.Label(self,textvariable = self.userName_label, anchor="w",bg = "white", fg="black")
		label_user.grid(column = 0, row = 0, sticky='EW')

		label_pass = Tkinter.Label(self,textvariable = self.passWord_label, anchor="w",bg = "white", fg="black")
		label_pass.grid(column = 0, row = 1, sticky='EW')

		label_vict = Tkinter.Label(self,textvariable = self.victName_label, anchor="w",bg = "white", fg="black")
		label_vict.grid(column = 0, row = 2, sticky='EW')

		label_cnt = Tkinter.Label(self,textvariable = self.count_label, anchor="w",bg = "white", fg="black")
		label_cnt.grid(column = 0, row = 3, sticky='EW')
		
		label_text = Tkinter.Label(self,textvariable = self.text_label, anchor="w",bg = "white", fg="black")
		label_text.grid(column = 0, row = 4, sticky='EW')

		
#Entry 
#===============================================================================
		self.user_entry = Tkinter.Entry(self,textvariable= self.userName)
		self.user_entry.grid(column=2, row=0, sticky='EW')

		self.user_pass = Tkinter.Entry(self,textvariable= self.passWord, show = '*')
		self.user_pass.grid(column=2, row=1, sticky='EW')

		self.user_vict = Tkinter.Entry(self,textvariable= self.victName)
		self.user_vict.grid(column=2, row=2, sticky='EW')

		self.user_count = Tkinter.Entry(self,textvariable= self.count)
		self.user_count.grid(column=2, row=3, sticky='EW')

		self.user_count = Tkinter.Entry(self,textvariable= self.text)
		self.user_count.grid(column=2, row=4, sticky='EW')
		
#Button
#===============================================================================
		button = Tkinter.Button(self,text='SpamBot', command = self.OnButtonClick)
		button.grid(column=2, row=5)
#		self.entryVariable = Tkinter.StringVar()
#		self.entry = Tkinter.Entry(self,textvariable = self.entryVariable)
#		self.entry.grid(column=0,row=0,sticky='EW')
#		self.entry.bind("<Return>", self.OnPressEnter)
#		self.entryVariable.set("Enter text here")

#		button = Tkinter.Button(self, text= 'Click me !', command=self.OnButtonClick)
#		button.grid(column=1, row = 0)

		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)

	def OnButtonClick(self):
		self.send_email()
#		self.labelVariable.set(self.entryVariable.get() + " You clicked the button !")

	def send_email(self):
		gmail_user = self.userName.get() #"smtp.python.netsec@gmail.com"
		gmail_pwd = self.passWord.get() #"InfoSecu"
		FROM = 'test@example.com'
		TO = [self.victName.get()] #must be a list
		SUBJECT = "Testing sending using gmail"
		TEXT = self.text.get() # "Testing sending mail using gmail servers"
		COUNT = self.count.get();
		# Prepare actual message
		message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
		""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
			#server = smtplib.SMTP(SERVER) 
		i = 0;face
		for i in range(COUNT):
			server = smtplib.SMTP("smtp.gmail.com", 587) 
			server.ehlo()
			server.starttls()
			server.login(gmail_user, gmail_pwd)
			server.sendmail(FROM, TO, message)
			#server.quit()
			server.close()
			print 'successfully sent the mail'

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('SpamBot')
	app.mainloop()
