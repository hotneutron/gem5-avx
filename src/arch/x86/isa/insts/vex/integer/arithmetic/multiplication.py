microcode = '''
def macroop VEX_MULX_R_R_R
{
    mulx rdx, regm, dataSize="32 << VEX_W"
    mulel reg2, dataSize="32 << VEX_W" 
    muleh reg1, dataSize="32 << VEX_W"
};

def macroop VEX_MULX_R_R_M
{
    ld t1, seg, sib, disp
    mulx rdx, t1, dataSize="32 << VEX_W"
    mulel reg2, dataSize="32 << VEX_W"
    muleh reg1, dataSize="32 << VEX_W"
};

def macroop VEX_MULX_R_R_P
{
    rdip t7
    ld t1, seg, riprel, disp
    mulx rdx, t1, dataSize="32 << VEX_W"
    mulel reg2, dataSize="32 << VEX_W"
    muleh reg1, dataSize="32 << VEX_W"
};

def macroop VEX_VPMULLD_XMM_XMM_XMM {
    gem5_avx_mullo_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPMULLD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mullo_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPMULLD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mullo_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPMULLD_YMM_YMM_YMM {
    gem5_avx_mullo_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPMULLD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mullo_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPMULLD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mullo_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPMULUDQ_XMM_XMM_XMM {
    gem5_avx_mul_epu64 xmm1, xmm2, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMULUDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_epu64 xmm1, xmm2, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMULUDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_epu64 xmm1, xmm2, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMULUDQ_YMM_YMM_YMM {
    gem5_avx_mul_epu64 ymm1, ymm2, ymmm, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMULUDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_epu64 ymm1, ymm2, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMULUDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_epu64 ymm1, ymm2, uvec1, srcSize=4, destSize=8, ext=YMM
};

'''
