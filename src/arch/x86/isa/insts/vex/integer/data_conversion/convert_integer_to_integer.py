microcode = '''
def macroop VEX_VPMOVSXDQ_XMM_XMM {
    gem5_avx_cvtepi32_epi64 xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVSXDQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVSXDQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVSXDQ_YMM_XMM {
    gem5_avx_cvtepi32_epi64 ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVSXDQ_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVSXDQ_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVZXDQ_XMM_XMM {
    gem5_avx_cvtepu32_epi64 xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVZXDQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVZXDQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVZXDQ_YMM_XMM {
    gem5_avx_cvtepu32_epi64 ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVZXDQ_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVZXDQ_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

'''
