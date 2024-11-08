# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
# class MotherBoard:
#     def __init__(self, name, cpu, *memory):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = memory[:self.total_mem_slots]
#
#     def get_config(self):
#         res = [f"Материнская плата: {self.name}", f"Центральынй процессор: {self.cpu.name}, {self.cpu.fr}",
#                f"Слотов памяти: {len(self.mem_slots)}", "Память: "]
#         for i in range(len(self.mem_slots)):
#             res[3] += f"{self.mem_slots[i].name} - {self.mem_slots[i].volume}"
#             if i != len(self.mem_slots)-1:
#                 res[3] += '; '
#         return res
#
#
#
# cpu1 = CPU("Intel", 3700)
# m1 = Memory("Kingston", 16)
# m2 = Memory("Kingston", 16)
#
# mb = MotherBoard("ASUS ABC 3034", cpu1, m1, m2)
#
# print(mb.get_config())
#


class CPU:
    def __init__(self, name, gh):
        self.name = name
        self.fr = gh


class Memory:
    def __init__(self, name, size):
        self.name = name
        self.volume = size

class MotherBoard:
    def __init__(self, name, cpu, *ms):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(ms)[:self.total_mem_slots]

    def get_config(self):
        return [f"Материнская плата: {self.name};",
              f"Центральный процессор: {self.cpu.name}, {self.cpu.fr};",
              f"Слотов памяти: {self.total_mem_slots};",
              # f"Память:", "; ".join([f"{self.mem_slots[i].name} - {self.mem_slots[i].volume}" for i in range(len(self.mem_slots))])]
              f"Память: {"; ".join(map(lambda i: f"{i.name} - {i.volume}", self.mem_slots))}"]


cp = CPU('Intel 7340', 3400)
m1 = Memory("Kingstone", 16)
m2 = Memory("Kingstone", 4)
mb = MotherBoard("AsRock", cp, m1, m2)

print(*mb.get_config())





















