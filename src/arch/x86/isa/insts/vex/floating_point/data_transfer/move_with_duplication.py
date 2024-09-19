microcode = '''
def macroop VEX_VMOVDDUP_XMM_XMM {
    gem5_avx_movedup_pd xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVDDUP_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_movedup_pd xmm, uvec1, size=8, ext=XMM
};

def macroop VEX_VMOVDDUP_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_movedup_pd xmm, uvec1, size=8, ext=XMM
};

def macroop VEX_VMOVDDUP_YMM_YMM {
    gem5_avx_movedup_pd ymm, ymmm, size=8, ext=YMM
};

def macroop VEX_VMOVDDUP_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_movedup_pd ymm, uvec1, size=8, ext=YMM
};

def macroop VEX_VMOVDDUP_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_movedup_pd ymm, uvec1, size=8, ext=YMM
};

# VEX_VMOVSLDUP
def macroop VEX_VMOVSLDUP_XMM_XMM {
    gem5_avx_moveldup_ps xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VMOVSLDUP_XMM_M {
    ldvec128ldup xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVSLDUP_XMM_P {
    rdip t7
    ldvec128ldup xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVSLDUP_YMM_YMM {
    gem5_avx_moveldup_ps ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VMOVSLDUP_YMM_M {
    ldvec256ldup ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVSLDUP_YMM_P {
    rdip t7
    ldvec256ldup ymm, seg, riprel, disp, dataSize=32
};

# VEX_VMOVSHDUP
def macroop VEX_VMOVSHDUP_XMM_XMM {
    gem5_avx_movehdup_ps xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VMOVSHDUP_XMM_M {
    ldvec128hdup xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVSHDUP_XMM_P {
    rdip t7
    ldvec128hdup xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVSHDUP_YMM_YMM {
    gem5_avx_movehdup_ps ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VMOVSHDUP_YMM_M {
    ldvec256hdup ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVSHDUP_YMM_P {
    rdip t7
    ldvec256hdup ymm, seg, riprel, disp, dataSize=32
};
'''
