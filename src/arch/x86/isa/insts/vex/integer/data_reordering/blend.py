microcode = '''
def macroop VEX_VPBLENDW_XMM_XMM_XMM_I {
    gem5_avx_blend_epi16 xmm1, xmm2, xmmm, size=2, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPBLENDW_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_blend_epi16 xmm1, xmm2, uvec1, size=2, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPBLENDW_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_blend_epi16 xmm1, xmm2, uvec1, size=2, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPBLENDW_YMM_YMM_YMM_I {
    gem5_avx_blend_epi16 ymm1, ymm2, ymmm, size=2, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPBLENDW_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_blend_epi16 ymm1, ymm2, uvec1, size=2, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPBLENDW_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_blend_epi16 ymm1, ymm2, uvec1, size=2, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPBLENDD_XMM_XMM_XMM_I {
    gem5_avx_blend_ps xmm1, xmm2, xmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPBLENDD_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_blend_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPBLENDD_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_blend_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPBLENDD_YMM_YMM_YMM_I {
    gem5_avx_blend_ps ymm1, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPBLENDD_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_blend_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPBLENDD_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_blend_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPBLENDVB_XMM_XMM_XMM_XMM {
    gem5_avx_blend_vb xmm1, xmm2, xmmm, xmm4, size=8, ext=XMM
};

def macroop VEX_VPBLENDVB_XMM_XMM_M_XMM {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_blend_vb xmm1, xmm2, uvec1, xmm4, size=8, ext=XMM
};

def macroop VEX_VPBLENDVB_XMM_XMM_P_XMM {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_blend_vb xmm1, xmm2, uvec1, xmm4, size=8, ext=XMM
};

def macroop VEX_VPBLENDVB_YMM_YMM_YMM_YMM {
    gem5_avx_blend_vb ymm1, ymm2, ymmm, ymm4, size=8, ext=YMM
};

def macroop VEX_VPBLENDVB_YMM_YMM_M_YMM {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_blend_vb ymm1, ymm2, uvec1, ymm4, size=8, ext=YMM
};

def macroop VEX_VPBLENDVB_YMM_YMM_P_YMM {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_blend_vb ymm1, ymm2, uvec1, ymm4, size=8, ext=YMM
};
'''
