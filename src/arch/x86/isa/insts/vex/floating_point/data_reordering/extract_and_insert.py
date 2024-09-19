microcode = '''
def macroop VEX_VINSERTPS_XMM_XMM_XMM_I {
    gem5_avx_insert_ps xmm1, xmm2, xmmm, size=4, ext="IMMEDIATE"
};

def macroop VEX_VINSERTPS_XMM_XMM_M_I {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=4
    gem5_avx_insert_ps xmm1, xmm2, uvec1, size=4, ext="IMMEDIATE & mask(6)"
};

def macroop VEX_VINSERTPS_XMM_XMM_P_I {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_insert_ps xmm1, xmm2, uvec1, size=4, ext="IMMEDIATE & mask(6)"
};

def macroop VEX_VINSERTF128_YMM_YMM_XMM_I {
    gem5_avx_insert_epu128 ymm1, ymm2, xmmm, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VINSERTF128_YMM_YMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VINSERTF128_YMM_YMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VEXTRACTF128_XMM_YMM_I {
    gem5_mm256_extractf128_si256 xmm, ymmm, size=32, ext="IMMEDIATE & mask(1)"
};

def macroop VEX_VEXTRACTF128_M_YMM_I {
    gem5_mm256_extractf128_si256 uvec1, ymm, size=32, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop VEX_VEXTRACTF128_P_YMM_I {
    rdip t7
    gem5_mm256_extractf128_si256 uvec1, ymm,  size=32, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop VEX_VEXTRACTF32X4_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop VEX_VEXTRACTF32X4_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop VEX_VEXTRACTF32X4_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop VEX_VEXTRACTF64X2_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop VEX_VEXTRACTF64X2_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop VEX_VEXTRACTF64X2_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

'''
