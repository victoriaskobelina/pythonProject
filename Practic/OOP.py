#Статические методы
class Comment:
    def __init__(self, text):
        self.text = text
    def merge_comments(first, second):
        return f"{first} {second}"
my_comment = Comment("My comment")
m_1 = Comment.merge_comments("Привет,","студент!")
print(m_1)
m_2 = Comment.merge_comments("Great","OK")
print(m_2)

class Comment:
    count = 0
def __init__(self, text):
    self.text = text
def upcount(self):
    self.count += 1
my_comment = Comment("My comment")
print(dir(my_comment))
#my_comment.upcount()
#print(my_comment.count)
#my_comment.upcount = 17
#print(my_comment.__dict__)
#print(Comment.count)
#print(my_comment.count)
#print(Comment.__dict__)