import dis, opcode

'''
form http://hi.baidu.com/tinyweb/item/923d012e8146d00872863ec0
Disassemble the bytesource object. bytesource can denote either a module, a class, a method, 
a function, or a code object. For a module, it disassembles all functions. For a class, it 
disassembles all methods. For a single code sequence, it prints one line per bytecode instruction. 
If no object is provided, it disassembles the last traceback.    
'''

class loaf:
        def __init__(self, a, b):
                self.a = a
                self.b = b
        def minus(self):
                return self.a - self.b
            
a = loaf(5, 3)
dis.dis(a)
HAVE_ARGUMENT = dis.HAVE_ARGUMENT
print HAVE_ARGUMENT

'''
c = a.minus.__code__
n = len(c.co_code)
hasname = dis.hasname
hasjrel = dis.hasjrel
haslocal = dis.haslocal
hasfree = dis.hasfree
i = 0
while i < n:
    op = ord(c.co_code[i])
    print opcode.opname[op]
    i = i + 1
    if op >= HAVE_ARGUMENT:
        oparg = ord(c.co_code[i]) + ord(c.co_code[i+1])*256
        if op in hasname:
            print 'name', c.co_names[oparg]
        elif op in hasjrel:
            print 'addr', i+oparg
        elif op in haslocal:
            print 'var', c.co_varnames[oparg]
        elif op in hasfree:
            if free is None:
                free = c.co_cellvars + c.co_freevars
            print 'free', free[oparg]
            
print dir(a.minus)
print a.minus.__self__.b
'''