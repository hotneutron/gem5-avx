microcode = '''
def macroop VEX_VHADDPS_XMM_XMM_XMM {
    gem5_avx_shuffle_ps uvec1, xmm2, xmmm, size=4, ext="0x88 |" + XMM
    gem5_avx_shuffle_ps uvec2, xmm2, xmmm, size=4, ext="0xDD |" + XMM
    gem5_avx_add_ps xmm1, uvec1, uvec2, size=4, ext=XMM
};

def macroop VEX_VHADDPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_shuffle_ps uvec2, xmm2, uvec1, size=4, ext="0x88 |" + XMM
    gem5_avx_shuffle_ps uvec3, xmm2, uvec1, size=4, ext="0xDD |" + XMM
    gem5_avx_add_ps xmm1, uvec2, uvec3, size=4, ext=XMM
};

def macroop VEX_VHADDPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_shuffle_ps uvec2, xmm2, uvec1, size=4, ext="0x88 |" + XMM
    gem5_avx_shuffle_ps uvec3, xmm2, uvec1, size=4, ext="0xDD |" + XMM
    gem5_avx_add_ps xmm1, uvec2, uvec3, size=4, ext=XMM
};

def macroop VEX_VHADDPS_YMM_YMM_YMM {
    gem5_avx_shuffle_ps uvec1, ymm2, ymmm, size=4, ext="0x88 |" + YMM
    gem5_avx_shuffle_ps uvec2, ymm2, ymmm, size=4, ext="0xDD |" + YMM
    gem5_avx_add_ps ymm1, uvec1, uvec2, size=4, ext=YMM
};

def macroop VEX_VHADDPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_shuffle_ps uvec2, ymm2, uvec1, size=4, ext="0x88 |" + YMM
    gem5_avx_shuffle_ps uvec3, ymm2, uvec1, size=4, ext="0xDD |" + YMM
    gem5_avx_add_ps ymm1, uvec2, uvec3, size=4, ext=YMM
};

def macroop VEX_VHADDPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_shuffle_ps uvec2, ymm2, uvec1, size=4, ext="0x88 |" + YMM
    gem5_avx_shuffle_ps uvec3, ymm2, uvec1, size=4, ext="0xDD |" + YMM
    gem5_avx_add_ps ymm1, uvec2, uvec3, size=4, ext=YMM
};

def macroop VEX_VHADDPD_XMM_XMM_XMM {
    gem5_avx_shuffle_pd uvec1, xmm2, xmmm, size=4, ext="0x0 |" + XMM
    gem5_avx_shuffle_pd uvec2, xmm2, xmmm, size=4, ext="0x3 |" + XMM
    gem5_avx_add_pd xmm1, uvec1, uvec2, size=8, ext=XMM
};

def macroop VEX_VHADDPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_shuffle_pd uvec2, xmm2, uvec1, size=4, ext="0x0 |" + XMM
    gem5_avx_shuffle_pd uvec3, xmm2, uvec1, size=4, ext="0x3 |" + XMM
    gem5_avx_add_pd xmm1, uvec2, uvec3, size=8, ext=XMM
};

def macroop VEX_VHADDPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_shuffle_pd uvec2, xmm2, uvec1, size=4, ext="0x0 |" + XMM
    gem5_avx_shuffle_pd uvec3, xmm2, uvec1, size=4, ext="0x3 |" + XMM
    gem5_avx_add_pd xmm1, uvec2, uvec3, size=8, ext=XMM
};

def macroop VEX_VHADDPD_YMM_YMM_YMM {
    gem5_avx_shuffle_pd uvec1, ymm2, ymmm, size=4, ext="0x0 |" + YMM
    gem5_avx_shuffle_pd uvec2, ymm2, ymmm, size=4, ext="0xf |" + YMM
    gem5_avx_add_pd ymm1, uvec1, uvec2, size=8, ext=YMM
};

def macroop VEX_VHADDPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_shuffle_pd uvec2, ymm2, uvec1, size=4, ext="0x0 |" + YMM
    gem5_avx_shuffle_pd uvec3, ymm2, uvec1, size=4, ext="0xf |" + YMM
    gem5_avx_add_pd ymm1, uvec2, uvec3, size=8, ext=YMM
};

def macroop VEX_VHADDPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_shuffle_pd uvec2, ymm2, uvec1, size=4, ext="0x0 |" + YMM
    gem5_avx_shuffle_pd uvec3, ymm2, uvec1, size=4, ext="0xf |" + YMM
    gem5_avx_add_pd ymm1, uvec2, uvec3, size=8, ext=YMM
};

'''
