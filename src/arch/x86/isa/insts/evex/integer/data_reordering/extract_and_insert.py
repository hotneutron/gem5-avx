microcode = '''
def macroop EVEX_VPEXTRB_R_XMM_I {
    gem5_mm_extract_epi8 reg, xmmm, "IMMEDIATE & mask(4)", size=1, ext=0
};

def macroop EVEX_VPEXTRB_M_XMM_I {
    gem5_mm_extract_epi8 t1, xmm, "IMMEDIATE & mask(4)", size=1, ext=0
    st t1, seg, sib, disp, dataSize=1
};

def macroop EVEX_VPEXTRB_P_XMM_I {
    rdip t7
    gem5_mm_extract_epi8 t1, xmm, "IMMEDIATE & mask(4)", size=1, ext=0
    st t1, seg, riprel, disp, dataSize=1
};

def macroop EVEX_VPEXTRW_R_XMM_I {
    gem5_mm_extract_epi16 reg, xmmm, "IMMEDIATE & mask(3)", size=2, ext=0
};

def macroop EVEX_VPEXTRW_M_XMM_I {
    gem5_mm_extract_epi16 t1, xmm, "IMMEDIATE & mask(3)", size=2, ext=0
    st t1, seg, sib, disp, dataSize=2
};

def macroop EVEX_VPEXTRW_P_XMM_I {
    rdip t7
    gem5_mm_extract_epi16 t1, xmm, "IMMEDIATE & mask(3)", size=2, ext=0
    st t1, seg, riprel, disp, dataSize=2
};

def macroop EVEX_VPEXTRD_R_XMM_I {
    gem5_mm_extract_epi32 reg, xmmm, "IMMEDIATE & mask(2)", size=4, ext=0
};

def macroop EVEX_VPEXTRD_M_XMM_I {
    gem5_mm_extract_epi32 t1, xmm, "IMMEDIATE & mask(2)", size=4, ext=0
    st t1, seg, sib, disp, dataSize=4
};

def macroop EVEX_VPEXTRD_P_XMM_I {
    rdip t7
    gem5_mm_extract_epi32 t1, xmm, "IMMEDIATE & mask(2)", size=4, ext=0
    st t1, seg, riprel, disp, dataSize=4
};

def macroop EVEX_VPEXTRQ_R_XMM_I {
    gem5_mm_extract_epi64 reg, xmmm, "IMMEDIATE & mask(1)", size=8, ext=0
};

def macroop EVEX_VPEXTRQ_M_XMM_I {
    gem5_mm_extract_epi64 t1, xmm, "IMMEDIATE & mask(1)", size=8, ext=0
    st t1, seg, sib, disp, dataSize=8
};

def macroop EVEX_VPEXTRQ_P_XMM_I {
    gem5_mm_extract_epi64 t1, xmm, "IMMEDIATE & mask(1)", size=8, ext=0
    st t1, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VPINSRD_XMM_XMM_R_I {
    gem5_avx_insert_epi32 xmm1, xmm2, regm, "IMMEDIATE & mask(2)", size=4, ext=1
};

def macroop EVEX_VPINSRD_XMM_XMM_M_I {
    ld t1, seg, sib, disp, dataSize=4
    gem5_avx_insert_epi32 xmm1, xmm2, t1, "IMMEDIATE & mask(2)", size=4, ext=1
};

def macroop EVEX_VPINSRD_XMM_XMM_P_I {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=4
    gem5_avx_insert_epi32 xmm1, xmm2, t1, "IMMEDIATE & mask(2)", size=4, ext=1
};

def macroop EVEX_VPINSRQ_XMM_XMM_R_I {
    gem5_avx_insert_epi64 xmm1, xmm2, regm, "IMMEDIATE & mask(1)", size=8, ext=1
};

def macroop EVEX_VPINSRQ_XMM_XMM_M_I {
    ld t1, seg, sib, disp, dataSize=8
    gem5_avx_insert_epi64 xmm1, xmm2, t1, "IMMEDIATE & mask(1)", size=8, ext=1
};

def macroop EVEX_VPINSRQ_XMM_XMM_P_I {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=8
    gem5_avx_insert_epi64 xmm1, xmm2, t1, "IMMEDIATE & mask(1)", size=8, ext=1
};

def macroop EVEX_VINSERTI32X4_YMM_YMM_XMM_I {
    gem5_avx_insert_epu128 ymm1, ymm2, xmmm, "IMMEDIATE", size=32, ext=YMM
};

def macroop EVEX_VINSERTI32X4_YMM_YMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop EVEX_VINSERTI32X4_YMM_YMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop EVEX_VINSERTI32X4_ZMM_ZMM_XMM_I {
    gem5_avx_insert_epu128 zmm1, zmm2, xmmm, "IMMEDIATE", size=32, ext=ZMM
};

def macroop EVEX_VINSERTI32X4_ZMM_ZMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_insert_epu128 zmm1, zmm2, uvec1, "IMMEDIATE", size=32, ext=ZMM
};

def macroop EVEX_VINSERTI32X4_ZMM_ZMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_insert_epu128 zmm1, zmm2, uvec1, "IMMEDIATE", size=32, ext=ZMM
};

def macroop EVEX_VEXTRACTI32X4_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTI32X4_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI32X4_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI32X4_XMM_ZMM_I {
    gem5_evex_extracti64x2 xmm, zmmm, size=8, ext="IMMEDIATE & mask(2)"
};

def macroop EVEX_VEXTRACTI32X4_M_ZMM_I {
    gem5_evex_extracti64x2 uvec1, zmm, size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI32X4_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, zmm,  size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI64X2_XMM_YMM_I {
    gem5_evex_extracti64x2 xmm, ymmm, size=8, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTI64X2_M_YMM_I {
    gem5_evex_extracti64x2 uvec1, ymm, size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI64X2_P_YMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, ymm,  size=8, ext="IMMEDIATE & mask(1)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI64X2_XMM_ZMM_I {
    gem5_evex_extracti64x2 xmm, zmmm, size=8, ext="IMMEDIATE & mask(2)"
};

def macroop EVEX_VEXTRACTI64X2_M_ZMM_I {
    gem5_evex_extracti64x2 uvec1, zmm, size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, sib, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI64X2_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x2 uvec1, zmm,  size=8, ext="IMMEDIATE & mask(2)"
    stvec128 uvec1, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VEXTRACTI32X8_YMM_ZMM_I {
    gem5_evex_extracti64x4 ymm, zmmm, size=64, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTI32X8_M_ZMM_I {
    gem5_evex_extracti64x4 uvec1, zmm, size=64, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, sib, disp, dataSize=32
};

def macroop EVEX_VEXTRACTI32X8_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x4 uvec1, zmm,  size=64, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VEXTRACTI64X4_YMM_ZMM_I {
    gem5_evex_extracti64x4 ymm, zmmm, size=64, ext="IMMEDIATE & mask(1)"
};

def macroop EVEX_VEXTRACTI64X4_M_ZMM_I {
    gem5_evex_extracti64x4 uvec1, zmm, size=64, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, sib, disp, dataSize=32
};

def macroop EVEX_VEXTRACTI64X4_P_ZMM_I {
    rdip t7
    gem5_evex_extracti64x4 uvec1, zmm,  size=64, ext="IMMEDIATE & mask(1)"
    stvec256 uvec1, seg, riprel, disp, dataSize=32
};

'''
