microcode = '''
def macroop VEX_VFNMADD132SS_XMM_XMM_XMM {
    gem5_avx_fnmadd132_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VFNMADD132SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fnmadd132_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFNMADD132SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fnmadd132_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFNMADD132SD_XMM_XMM_XMM {
    gem5_avx_fnmadd132_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop VEX_VFNMADD132SD_XMM_XMM_M {
    gem5_mm_load_sd uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fnmadd132_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFNMADD132SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_sd uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fnmadd132_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFNMADD213SS_XMM_XMM_XMM {
    gem5_avx_fnmadd213_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VFNMADD213SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fnmadd213_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFNMADD213SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fnmadd213_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFNMADD213SD_XMM_XMM_XMM {
    gem5_avx_fnmadd213_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop VEX_VFNMADD213SD_XMM_XMM_M {
    gem5_mm_load_sd uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fnmadd213_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFNMADD213SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_sd uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fnmadd213_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFNMADD231SS_XMM_XMM_XMM {
    gem5_avx_fnmadd231_ss xmm, xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VFNMADD231SS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_fnmadd231_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFNMADD231SS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_fnmadd231_ss xmm, xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VFNMADD231SD_XMM_XMM_XMM {
    gem5_avx_fnmadd231_sd xmm, xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop VEX_VFNMADD231SD_XMM_XMM_M {
    gem5_mm_load_sd uvec1, seg, sib, disp, dataSize=8
    gem5_avx_fnmadd231_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFNMADD231SD_XMM_XMM_P {
    rdip t7
    gem5_mm_load_sd uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_fnmadd231_sd xmm, xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop VEX_VFNMADD132PS_XMM_XMM_XMM {
    gem5_avx_fnmadd132_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFNMADD132PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fnmadd132_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFNMADD132PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fnmadd132_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFNMADD213PS_XMM_XMM_XMM {
    gem5_avx_fnmadd213_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFNMADD213PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fnmadd213_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFNMADD213PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fnmadd213_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFNMADD231PS_XMM_XMM_XMM {
    gem5_avx_fnmadd231_ps xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VFNMADD231PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fnmadd231_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFNMADD231PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fnmadd231_ps xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VFNMADD132PD_XMM_XMM_XMM {
    gem5_avx_fnmadd132_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFNMADD132PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fnmadd132_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFNMADD132PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fnmadd132_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFNMADD213PD_XMM_XMM_XMM {
    gem5_avx_fnmadd213_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFNMADD213PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fnmadd213_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFNMADD213PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fnmadd213_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFNMADD231PD_XMM_XMM_XMM {
    gem5_avx_fnmadd231_pd xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VFNMADD231PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_fnmadd231_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFNMADD231PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_fnmadd231_pd xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VFNMADD132PS_YMM_YMM_YMM {
    gem5_avx_fnmadd132_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFNMADD132PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fnmadd132_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFNMADD132PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fnmadd132_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFNMADD213PS_YMM_YMM_YMM {
    gem5_avx_fnmadd213_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFNMADD213PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fnmadd213_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFNMADD213PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fnmadd213_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFNMADD231PS_YMM_YMM_YMM {
    gem5_avx_fnmadd231_ps ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VFNMADD231PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fnmadd231_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFNMADD231PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fnmadd231_ps ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VFNMADD132PD_YMM_YMM_YMM {
    gem5_avx_fnmadd132_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFNMADD132PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fnmadd132_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFNMADD132PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fnmadd132_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFNMADD213PD_YMM_YMM_YMM {
    gem5_avx_fnmadd213_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFNMADD213PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fnmadd213_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFNMADD213PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fnmadd213_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFNMADD231PD_YMM_YMM_YMM {
    gem5_avx_fnmadd231_pd ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VFNMADD231PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_fnmadd231_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VFNMADD231PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_fnmadd231_pd ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

'''
