microcode = '''
def macroop EVEX_VINSERTPS_XMM_XMM_XMM_I {
    gem5_avx_insert_ps xmm1, xmm2, xmmm, size=4, ext="IMMEDIATE"
};

def macroop EVEX_VINSERTPS_XMM_XMM_M_I {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=4
    gem5_avx_insert_ps xmm1, xmm2, uvec1, size=4, ext="IMMEDIATE & mask(6)"
};

def macroop EVEX_VINSERTPS_XMM_XMM_P_I {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_insert_ps xmm1, xmm2, uvec1, size=4, ext="IMMEDIATE & mask(6)"
};

def macroop EVEX_VINSERTF32X4_YMM_YMM_XMM_I {
    gem5_avx_insert_epu128 ymm1, ymm2, xmmm, "IMMEDIATE", size=4, ext=YMM
};

def macroop EVEX_VINSERTF32X4_YMM_YMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=4, ext=YMM
};

def macroop EVEX_VINSERTF32X4_YMM_YMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=4, ext=YMM
};

def macroop EVEX_VINSERTF32X4_ZMM_ZMM_XMM_I {
    gem5_avx_insert_epu128 zmm1, zmm2, xmmm, "IMMEDIATE", size=4, ext=ZMM
};

def macroop EVEX_VINSERTF32X4_ZMM_ZMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 zmm1, zmm2, uvec1, "IMMEDIATE", size=4, ext=ZMM
};

def macroop EVEX_VINSERTF32X4_ZMM_ZMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 zmm1, zmm2, uvec1, "IMMEDIATE", size=4, ext=ZMM
};

def macroop EVEX_VINSERTF64X2_YMM_YMM_XMM_I {
    gem5_avx_insert_epu128 ymm1, ymm2, xmmm, "IMMEDIATE", size=8, ext=YMM
};

def macroop EVEX_VINSERTF64X2_YMM_YMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=8, ext=YMM
};

def macroop EVEX_VINSERTF64X2_YMM_YMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=8, ext=YMM
};

def macroop EVEX_VINSERTF64X2_ZMM_ZMM_XMM_I {
    gem5_avx_insert_epu128 zmm1, zmm2, xmmm, "IMMEDIATE", size=8, ext=ZMM
};

def macroop EVEX_VINSERTF64X2_ZMM_ZMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 zmm1, zmm2, uvec1, "IMMEDIATE", size=8, ext=ZMM
};

def macroop EVEX_VINSERTF64X2_ZMM_ZMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 zmm1, zmm2, uvec1, "IMMEDIATE", size=8, ext=ZMM
};

def macroop EVEX_VINSERTF64X4_ZMM_ZMM_YMM_I {
    gem5_evex_inserti64x4 zmm1, zmm2, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VINSERTF64X4_ZMM_ZMM_M_I {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_evex_inserti64x4 zmm1, zmm2, uvec1, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VINSERTF64X4_ZMM_ZMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_evex_inserti64x4 zmm1, zmm2, uvec1, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_EVEXTRACTF128_XMM_YMM_I {
    gem5_mm256_extractf128_si256 xmm, ymmm, size=32, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_EVEXTRACTF128_M_YMM_I {
    gem5_mm256_extractf128_si256 uvec1, ymm, size=32, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_EVEXTRACTF128_P_YMM_I {
    rdip t7
    gem5_mm256_extractf128_si256 uvec1, ymm,  size=32, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF32X4_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTF32X4_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF32X4_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF32X4_XMM_ZMM_I {
    gem5_evex_extracti64x2 xmm, zmmm, size=8, ext="IMMEDIATE & mask(2)"
};

def macroop EVEX_VEXTRACTF32X4_M_ZMM_I {
    gem5_evex_extracti64x2 uvec1, zmm, size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF32X4_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, zmm,  size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF64X2_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTF64X2_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF64X2_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF64X2_XMM_ZMM_I {
    gem5_evex_extracti64x2 xmm, zmmm, size=8, ext="IMMEDIATE & mask(2)"
};

def macroop EVEX_VEXTRACTF64X2_M_ZMM_I {
    gem5_evex_extracti64x2 uvec1, zmm, size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF64X2_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, zmm,  size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTF32X8_YMM_ZMM_I {
    gem5_evex_extracti64x4 ymm, zmmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTF32X8_M_ZMM_I {
    gem5_evex_extracti64x4 uvec1, zmm, size=8, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, sib, disp, dataSize=32
};

def macroop EVEX_VEXTRACTF32X8_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x4 uvec1, zmm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VEXTRACTF64X4_YMM_ZMM_I {
    gem5_evex_extracti64x4 ymm, zmmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTF64X4_M_ZMM_I {
    gem5_evex_extracti64x4 uvec1, zmm, size=8, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, sib, disp, dataSize=32
};

def macroop EVEX_VEXTRACTF64X4_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x4 uvec1, zmm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, riprel, disp, dataSize=32
};

'''
