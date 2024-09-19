microcode = '''
def macroop VEX_VPEXTRD_R_XMM_I {
    gem5_mm_extract_epi32 reg, xmmm, "IMMEDIATE & mask(2)", size=4, ext=0
};

def macroop VEX_VPEXTRD_M_XMM_I {
    gem5_mm_extract_epi32 t1, xmm, "IMMEDIATE & mask(2)", size=4, ext=0
    st t1, seg, sib, disp, dataSize=4
};

def macroop VEX_VPEXTRD_P_XMM_I {
    rdip t7
    gem5_mm_extract_epi32 t1, xmm, "IMMEDIATE & mask(2)", size=4, ext=0
    st t1, seg, riprel, disp, dataSize=4
};

def macroop VEX_VPEXTRQ_R_XMM_I {
    gem5_mm_extract_epi64 reg, xmmm, "IMMEDIATE & mask(1)", size=8, ext=0
};

def macroop VEX_VPEXTRQ_M_XMM_I {
    gem5_mm_extract_epi64 t1, xmm, "IMMEDIATE & mask(1)", size=8, ext=0
    st t1, seg, sib, disp, dataSize=8
};

def macroop VEX_VPEXTRQ_P_XMM_I {
    gem5_mm_extract_epi64 t1, xmm, "IMMEDIATE & mask(1)", size=8, ext=0
    st t1, seg, riprel, disp, dataSize=8
};

def macroop VEX_VPINSRD_XMM_XMM_R_I {
    gem5_avx_insert_epi32 xmm1, xmm2, regm, "IMMEDIATE & mask(2)", size=4, ext=1
};

def macroop VEX_VPINSRD_XMM_XMM_M_I {
    ld t1, seg, sib, disp, dataSize=4
    gem5_avx_insert_epi32 xmm1, xmm2, t1, "IMMEDIATE & mask(2)", size=4, ext=1
};

def macroop VEX_VPINSRD_XMM_XMM_P_I {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=4
    gem5_avx_insert_epi32 xmm1, xmm2, t1, "IMMEDIATE & mask(2)", size=4, ext=1
};

def macroop VEX_VPINSRQ_XMM_XMM_R_I {
    gem5_avx_insert_epi64 xmm1, xmm2, regm, "IMMEDIATE & mask(1)", size=8, ext=1
};

def macroop VEX_VPINSRQ_XMM_XMM_M_I {
    ld t1, seg, sib, disp, dataSize=8
    gem5_avx_insert_epi64 xmm1, xmm2, t1, "IMMEDIATE & mask(1)", size=8, ext=1
};

def macroop VEX_VPINSRQ_XMM_XMM_P_I {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=8
    gem5_avx_insert_epi64 xmm1, xmm2, t1, "IMMEDIATE & mask(1)", size=8, ext=1
};

def macroop VEX_VINSERTI128_YMM_YMM_XMM_I {
    gem5_avx_insert_epu128 ymm1, ymm2, xmmm, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VINSERTI128_YMM_YMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VINSERTI128_YMM_YMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VEXTRACTI128_XMM_YMM_I {
    gem5_mm256_extractf128_si256 xmm, ymmm, size=32, ext="IMMEDIATE & mask(1)"
};

def macroop VEX_VEXTRACTI128_M_YMM_I {
    gem5_mm256_extractf128_si256 uvec1, ymm, size=32, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop VEX_VEXTRACTI128_P_YMM_I {
    rdip t7
    gem5_mm256_extractf128_si256 uvec1, ymm,  size=32, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop VEX_VEXTRACTI32X4_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop VEX_VEXTRACTI32X4_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop VEX_VEXTRACTI32X4_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop VEX_VEXTRACTI64X2_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop VEX_VEXTRACTI64X2_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop VEX_VEXTRACTI64X2_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

'''
