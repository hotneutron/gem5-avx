microcode = '''
def macroop VEX_VFMSUB132SS_XMM_XMM_XMM {
    gem5_avx_fmsub132_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VFMSUB132SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fmsub132_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFMSUB132SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fmsub132_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFMSUB132SD_XMM_XMM_XMM {
    gem5_avx_fmsub132_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop VEX_VFMSUB132SD_XMM_XMM_M {
    gem5_mm_load_sd uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fmsub132_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFMSUB132SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_sd uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fmsub132_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFMSUB213SS_XMM_XMM_XMM {
    gem5_avx_fmsub213_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VFMSUB213SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fmsub213_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFMSUB213SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fmsub213_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFMSUB213SD_XMM_XMM_XMM {
    gem5_avx_fmsub213_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop VEX_VFMSUB213SD_XMM_XMM_M {
    gem5_mm_load_sd uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fmsub213_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFMSUB213SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_sd uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fmsub213_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFMSUB231SS_XMM_XMM_XMM {
    gem5_avx_fmsub231_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VFMSUB231SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fmsub231_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFMSUB231SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fmsub231_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFMSUB231SD_XMM_XMM_XMM {
    gem5_avx_fmsub231_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop VEX_VFMSUB231SD_XMM_XMM_M {
    gem5_mm_load_sd uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fmsub231_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFMSUB231SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_sd uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fmsub231_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFMSUB132PS_XMM_XMM_XMM {
    gem5_avx_fmsub132_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFMSUB132PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmsub132_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMSUB132PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmsub132_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMSUB213PS_XMM_XMM_XMM {
    gem5_avx_fmsub213_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFMSUB213PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmsub213_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMSUB213PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmsub213_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMSUB231PS_XMM_XMM_XMM {
    gem5_avx_fmsub231_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFMSUB231PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmsub231_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMSUB231PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmsub231_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFMSUB132PD_XMM_XMM_XMM {
    gem5_avx_fmsub132_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFMSUB132PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmsub132_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMSUB132PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmsub132_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMSUB213PD_XMM_XMM_XMM {
    gem5_avx_fmsub213_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFMSUB213PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmsub213_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMSUB213PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmsub213_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMSUB231PD_XMM_XMM_XMM {
    gem5_avx_fmsub231_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFMSUB231PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fmsub231_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMSUB231PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fmsub231_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFMSUB132PS_YMM_YMM_YMM {
    gem5_avx_fmsub132_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFMSUB132PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmsub132_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMSUB132PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmsub132_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMSUB213PS_YMM_YMM_YMM {
    gem5_avx_fmsub213_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFMSUB213PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmsub213_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMSUB213PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmsub213_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMSUB231PS_YMM_YMM_YMM {
    gem5_avx_fmsub231_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFMSUB231PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmsub231_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMSUB231PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmsub231_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFMSUB132PD_YMM_YMM_YMM {
    gem5_avx_fmsub132_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFMSUB132PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmsub132_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMSUB132PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmsub132_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMSUB213PD_YMM_YMM_YMM {
    gem5_avx_fmsub213_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFMSUB213PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmsub213_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMSUB213PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmsub213_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMSUB231PD_YMM_YMM_YMM {
    gem5_avx_fmsub231_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFMSUB231PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fmsub231_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFMSUB231PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fmsub231_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

'''
