microcode = '''
def macroop VEX_VPTEST_XMM_XMM
{
    gem5_mm256_testc xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VPTEST_XMM_M
{
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm256_testc xmm, uvec1, size=8, ext=XMM
};

def macroop VEX_VPTEST_XMM_P
{
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm256_testc xmm, uvec1, size=8, ext=XMM
};

def macroop VEX_VPTEST_YMM_YMM
{
    gem5_mm256_testc ymm, ymmm, size=8, ext=YMM
};

def macroop VEX_VPTEST_YMM_M
{
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mm256_testc ymm, uvec1, size=8, ext=YMM
};

def macroop VEX_VPTEST_YMM_P
{
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mm256_testc ymm, uvec1, size=8, ext=YMM
};

def macroop VEX_KORTESTB_K_K {
    gem5_avx_kortest k, km, size=1, ext=0
};

def macroop VEX_KORTESTW_K_K {
    gem5_avx_kortest k, km, size=2, ext=0
};

def macroop VEX_KORTESTD_K_K {
    gem5_avx_kortest k, km, size=4, ext=0
};

def macroop VEX_KORTESTQ_K_K {
    gem5_avx_kortest k, km, size=8, ext=0
};

'''
