microcode = '''
def macroop EVEX_VBLENDMPS_XMM_XMM_XMM_K {
    gem5_mask_blend_epi32 xmm1, xmm2, xmmm, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VBLENDMPS_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_blend_epi32 xmm1, xmm2, uvec1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VBLENDMPS_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_blend_epi32 xmm1, xmm2, uvec1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VBLENDMPS_YMM_YMM_YMM_K {
    gem5_mask_blend_epi32 ymm1, ymm2, ymmm, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VBLENDMPS_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_blend_epi32 ymm1, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VBLENDMPS_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_blend_epi32 ymm1, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VBLENDMPS_ZMM_ZMM_ZMM_K {
    gem5_mask_blend_epi32 zmm1, zmm2, zmmm, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VBLENDMPS_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_blend_epi32 zmm1, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VBLENDMPS_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_blend_epi32 zmm1, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VBLENDMPD_XMM_XMM_XMM_K {
    gem5_mask_blend_epi64 xmm1, xmm2, xmmm, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VBLENDMPD_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_blend_epi64 xmm1, xmm2, uvec1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VBLENDMPD_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_blend_epi64 xmm1, xmm2, uvec1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VBLENDMPD_YMM_YMM_YMM_K {
    gem5_mask_blend_epi64 ymm1, ymm2, ymmm, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VBLENDMPD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_blend_epi64 ymm1, ymm2, uvec1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VBLENDMPD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_blend_epi64 ymm1, ymm2, uvec1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VBLENDMPD_ZMM_ZMM_ZMM_K {
    gem5_mask_blend_epi64 zmm1, zmm2, zmmm, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VBLENDMPD_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_blend_epi64 zmm1, zmm2, uvec1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VBLENDMPD_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_blend_epi64 zmm1, zmm2, uvec1, opmask=opmask, size=8, ext=ZMM
};

'''
