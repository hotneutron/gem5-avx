microcode = '''
def macroop BLENDPS_XMM_XMM_I {
    gem5_mm_blend_ps xmm, xmm, xmmm, size=4, ext="IMMEDIATE"
};

def macroop BLENDPS_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_blend_ps xmm, xmm, uvec1, size=4, ext="IMMEDIATE"
};

def macroop BLENDPS_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_blend_ps xmm, xmm, uvec1, size=4, ext="IMMEDIATE"
};

def macroop BLENDPD_XMM_XMM_I {
    gem5_mm_blend_pd xmm, xmm, xmmm, size=8, ext="IMMEDIATE"
};

def macroop BLENDPD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_blend_pd xmm, xmm, uvec1, size=8, ext="IMMEDIATE"
};

def macroop BLENDPD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_blend_pd xmm, xmm, uvec1, size=8, ext="IMMEDIATE"
};

def macroop BLENDVPS_XMM_XMM {
    gem5_mm_blendv_ps xmm, xmm, xmmm, size=4
};

def macroop BLENDVPS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_blendv_ps xmm, xmm, uvec1, size=4
};

def macroop BLENDVPS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_blendv_ps xmm, xmm, uvec1, size=4
};

def macroop BLENDVPD_XMM_XMM {
    gem5_mm_blendv_pd xmm, xmm, xmmm, size=8
};

def macroop BLENDVPD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_blendv_pd xmm, xmm, uvec1, size=8
};

def macroop BLENDVPD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_blendv_pd xmm, xmm, uvec1, size=8
};
'''
