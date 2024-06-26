from datetime import datetime, timedelta
import hashlib

class User:
    def __init__(self, user_id ,name, password, email) -> None:
        self.user_id=user_id
        self.name=name
        self.password=self.hash_password(password)
        self.email=email

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest

    def authenticate(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest

class Admin:
    def __init__(self, admin_id ,name, password, email) -> None:
        self.admin_id=admin_id
        self.name=name
        self.password=self.hash_password(password)
        # self.email=email

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest

    def authenticate(self, password):
        return self.password == hashlib.sha256(password.encode()).hexdigest
    
    def create_election(self, election_name, start_time, end_time, candidates):
        return Election(election_name,start_time,end_time,candidates)

class Election:
    def __init__(self, election_name,start_time,end_time,candidates) -> None:
        self.name=election_name
        self.start_time=start_time
        self.end_time=end_time
        # self.candidates=
    
    def is_active(self):
        return self.start_time<=datetime.now()<=self.end_time
    
    def cast_vote(self, user_id, candidate_id):
        if self.is_active():
            raise Exception("Election is not active")
        if candidate_id not in self.candidates:
            raise Exception("Innvalid Excetion")
        self.vote[user_id]=candidate_id
    
    def get_result(self):
        result= {can:0 for can in self.candidate}
        for vote in self.votes.values():
            result[vote]+=1
        return result

class Candidate:
    def __init__(self, candidate_id, name, party) :
        self.candidate_id=candidate_id
        self.name=name
        self.party=party
    
class Notification:
    @staticmethod
    def send_email(email, message):
        print(f"Sending email to {email}: {message}")

if __name__=='__main__':
    candidate=[
        Candidate(1,"Alice Johnson", "BJP"),
        Candidate(2, "Bob Smith", "Congress")
    ]
    
    admin=Admin(1,"Neeraj", "adminpass")

    election=admin.create_election(
        "2024 President Election",
        datetime.now(),
        datetime.now+timedelta(days=1),
        candidates=candidate
    )

    user =User(1,"Rahul", "userpass", "abc@gmail.com")

    # if user.authenticate("userpass"):
    #     elec
        
