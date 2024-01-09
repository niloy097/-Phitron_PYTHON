class A:
    def __init__(self, value):
        value = 3
        self.value = value
    def change(self):
        self.value = 12

ans = []
let = A(13)
ans.append(let.value)
let.change()
ans.append(let.value)
print(ans)