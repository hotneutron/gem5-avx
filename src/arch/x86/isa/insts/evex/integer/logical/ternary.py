microcode = '''
def macroop EVEX_VPTERNLOGD_XMM_XMM_XMM_I {
    gem5_evex_ternarylogic_epi32 xmm, xmm, xmm2, xmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPTERNLOGD_XMM_XMM_M_I  {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_evex_ternarylogic_epi32 xmm, xmm, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPTERNLOGD_XMM_XMM_P_I  {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_evex_ternarylogic_epi32 xmm, xmm, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPTERNLOGD_YMM_YMM_YMM_I  {
    gem5_evex_ternarylogic_epi32 ymm, ymm, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPTERNLOGD_YMM_YMM_M_I  {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_evex_ternarylogic_epi32 ymm, ymm, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPTERNLOGD_YMM_YMM_P_I  {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_evex_ternarylogic_epi32 ymm, ymm, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPTERNLOGD_ZMM_ZMM_ZMM_I  {
    gem5_evex_ternarylogic_epi32 zmm, zmm, zmm2, zmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPTERNLOGD_ZMM_ZMM_M_I  {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_evex_ternarylogic_epi32 zmm, zmm, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPTERNLOGD_ZMM_ZMM_P_I  {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_evex_ternarylogic_epi32 zmm, zmm, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPTERNLOGQ_XMM_XMM_XMM_I  {
    gem5_evex_ternarylogic_epi64 xmm, xmm, xmm2, xmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPTERNLOGQ_XMM_XMM_M_I  {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_evex_ternarylogic_epi64 xmm, xmm, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPTERNLOGQ_XMM_XMM_P_I  {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_evex_ternarylogic_epi64 xmm, xmm, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPTERNLOGQ_YMM_YMM_YMM_I  {
    gem5_evex_ternarylogic_epi64 ymm, ymm, ymm2, ymmm, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPTERNLOGQ_YMM_YMM_M_I  {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_evex_ternarylogic_epi64 ymm, ymm, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPTERNLOGQ_YMM_YMM_P_I  {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_evex_ternarylogic_epi64 ymm, ymm, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPTERNLOGQ_ZMM_ZMM_ZMM_I  {
    gem5_evex_ternarylogic_epi64 zmm, zmm, zmm2, zmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPTERNLOGQ_ZMM_ZMM_M_I  {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_evex_ternarylogic_epi64 zmm, zmm, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPTERNLOGQ_ZMM_ZMM_P_I  {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_evex_ternarylogic_epi64 zmm, zmm, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

'''
