microcode = '''
def macroop PBLENDVB_XMM_XMM {
    gem5_mm_blendv_epi8 xmm, xmm, xmmm, size=4
};

def macroop PBLENDVB_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_blendv_epi8 xmm, xmm, uvec1, size=4
};

def macroop PBLENDVB_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_blendv_epi8 xmm, xmm, uvec1, size=4
};

def macroop PBLENDW_XMM_XMM_I {
    gem5_mm_blend_epi16 xmm, xmm, xmmm, size=2, ext=imm
};

def macroop PBLENDW_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm_blend_epi16 xmm, xmm, uvec1, size=2, ext=imm
};

def macroop PBLENDW_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm_blend_epi16 xmm, xmm, uvec1, size=2, ext=imm
};
'''
