microcode = '''
def macroop VEX_VPMADDWD_XMM_XMM {
    gem5_avx_madd_epi16 xmm, xmm, xmmm, srcSize=2, destSize=4, ext = Signed
};

def macroop VEX_VPMADDWD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_madd_epi16 xmm, xmm, uvec1, srcSize=2, destSize=4, ext = Signed
};

def macroop VEX_VPMADDWD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_madd_epi16 xmm, xmm, uvec1, srcSize=2, destSize=4, ext = Signed
};

def macroop VEX_VPMADDWD_YMM_YMM {
    gem5_avx_madd_epi16 ymm, ymm, ymmm, srcSize=2, destSize=4, ext = Signed
};

def macroop VEX_VPMADDWD_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_madd_epi16 ymm, ymm, uvec1, srcSize=2, destSize=4, ext = Signed
};

def macroop VEX_VPMADDWD_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_madd_epi16 ymm, ymm, uvec1, srcSize=2, destSize=4, ext = Signed
};

'''
