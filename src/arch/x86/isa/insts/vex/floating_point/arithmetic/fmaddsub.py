microcode = '''
def macroop VEX_VFMADDSUB132PS_XMM_XMM_XMM {
    gem5_avx_fmaddsub132_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB132PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub132_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB132PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub132_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB132PS_YMM_YMM_YMM {
    gem5_avx_fmaddsub132_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB132PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub132_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB132PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub132_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB213PS_XMM_XMM_XMM {
    gem5_avx_fmaddsub213_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB213PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub213_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB213PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub213_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB213PS_YMM_YMM_YMM {
    gem5_avx_fmaddsub213_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB213PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub213_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB213PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub213_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB231PS_XMM_XMM_XMM {
    gem5_avx_fmaddsub231_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB231PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub231_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB231PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub231_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMADDSUB231PS_YMM_YMM_YMM {
    gem5_avx_fmaddsub231_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB231PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub231_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB231PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub231_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMADDSUB132PD_XMM_XMM_XMM {
    gem5_avx_fmaddsub132_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB132PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub132_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB132PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub132_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB132PD_YMM_YMM_YMM {
    gem5_avx_fmaddsub132_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB132PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub132_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB132PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub132_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB213PD_XMM_XMM_XMM {
    gem5_avx_fmaddsub213_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB213PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub213_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB213PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub213_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB213PD_YMM_YMM_YMM {
    gem5_avx_fmaddsub213_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB213PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub213_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB213PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub213_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB231PD_XMM_XMM_XMM {
    gem5_avx_fmaddsub231_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB231PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub231_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB231PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub231_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMADDSUB231PD_YMM_YMM_YMM {
    gem5_avx_fmaddsub231_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB231PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub231_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMADDSUB231PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub231_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMSUBADD132PS_XMM_XMM_XMM {
    gem5_avx_fmaddsub132_ps xmm, xmm1, xmm2, xmmm, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD132PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub132_ps xmm, xmm1, xmm2, uvec1, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD132PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub132_ps xmm, xmm1, xmm2, uvec1, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD132PS_YMM_YMM_YMM {
    gem5_avx_fmaddsub132_ps ymm, ymm1, ymm2, ymmm, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD132PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub132_ps ymm, ymm1, ymm2, uvec1, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD132PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub132_ps ymm, ymm1, ymm2, uvec1, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD213PS_XMM_XMM_XMM {
    gem5_avx_fmaddsub213_ps xmm, xmm1, xmm2, xmmm, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD213PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub213_ps xmm, xmm1, xmm2, uvec1, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD213PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub213_ps xmm, xmm1, xmm2, uvec1, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD213PS_YMM_YMM_YMM {
    gem5_avx_fmaddsub213_ps ymm, ymm1, ymm2, ymmm, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD213PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub213_ps ymm, ymm1, ymm2, uvec1, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD213PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub213_ps ymm, ymm1, ymm2, uvec1, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD231PS_XMM_XMM_XMM {
    gem5_avx_fmaddsub231_ps xmm, xmm1, xmm2, xmmm, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD231PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub231_ps xmm, xmm1, xmm2, uvec1, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD231PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub231_ps xmm, xmm1, xmm2, uvec1, size=4, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD231PS_YMM_YMM_YMM {
    gem5_avx_fmaddsub231_ps ymm, ymm1, ymm2, ymmm, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD231PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub231_ps ymm, ymm1, ymm2, uvec1, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD231PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub231_ps ymm, ymm1, ymm2, uvec1, size=4, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD132PD_XMM_XMM_XMM {
    gem5_avx_fmaddsub132_pd xmm, xmm1, xmm2, xmmm, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD132PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub132_pd xmm, xmm1, xmm2, uvec1, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD132PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub132_pd xmm, xmm1, xmm2, uvec1, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD132PD_YMM_YMM_YMM {
    gem5_avx_fmaddsub132_pd ymm, ymm1, ymm2, ymmm, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD132PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub132_pd ymm, ymm1, ymm2, uvec1, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD132PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub132_pd ymm, ymm1, ymm2, uvec1, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD213PD_XMM_XMM_XMM {
    gem5_avx_fmaddsub213_pd xmm, xmm1, xmm2, xmmm, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD213PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub213_pd xmm, xmm1, xmm2, uvec1, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD213PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub213_pd xmm, xmm1, xmm2, uvec1, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD213PD_YMM_YMM_YMM {
    gem5_avx_fmaddsub213_pd ymm, ymm1, ymm2, ymmm, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD213PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub213_pd ymm, ymm1, ymm2, uvec1, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD213PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub213_pd ymm, ymm1, ymm2, uvec1, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD231PD_XMM_XMM_XMM {
    gem5_avx_fmaddsub231_pd xmm, xmm1, xmm2, xmmm, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD231PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmaddsub231_pd xmm, xmm1, xmm2, uvec1, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD231PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmaddsub231_pd xmm, xmm1, xmm2, uvec1, size=8, ext="1 |" + XMM
};

def macroop VEX_VFMSUBADD231PD_YMM_YMM_YMM {
    gem5_avx_fmaddsub231_pd ymm, ymm1, ymm2, ymmm, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD231PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmaddsub231_pd ymm, ymm1, ymm2, uvec1, size=8, ext="1 |" + YMM
};

def macroop VEX_VFMSUBADD231PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmaddsub231_pd ymm, ymm1, ymm2, uvec1, size=8, ext="1 |" + YMM
};

'''
