microcode = '''
def macroop PTEST_XMM_XMM
{
    gem5_mm_testc_si128 xmm, xmmm, size=8, ext=2
};

def macroop PTEST_XMM_M
{
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_testc_si128 xmm, uvec1, size=8, ext=2
};

def macroop PTEST_XMM_P
{
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_testc_si128 xmm, uvec1, size=8, ext=2
};

'''
