setYMMAllRegTemplate = '''
    lymmallimm "InstRegIndex(VECTORREG_YMM(%(idx)i))", 0
'''

setYMMUpperRegTemplate = '''
    lymmupperimm "InstRegIndex(VECTORREG_YMM(%(idx)i))", 0
'''

setYMMAllRegs = \
    "".join([setYMMAllRegTemplate % { "idx" : i }
             for i in range(16)])

setYMMUpperRegs = \
    "".join([setYMMUpperRegTemplate % { "idx" : i }
             for i in range(16)])

microcode = '''
def macroop VEX_VZEROALL {
''' + setYMMAllRegs + '''
};

def macroop VEX_VZEROUPPER {
''' + setYMMUpperRegs + '''
};

'''
