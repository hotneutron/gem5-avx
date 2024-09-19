microcode = '''
def macroop EVEX_VBROADCASTSS_XMM_XMM {
    gem5_avx_broadcast_ss xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VBROADCASTSS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_broadcast_ss xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VBROADCASTSS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_broadcast_ss xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VBROADCASTSS_YMM_XMM {
    gem5_avx_broadcast_ss ymm, xmmm, size=4, ext=YMM
};

def macroop EVEX_VBROADCASTSS_YMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_broadcast_ss  ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VBROADCASTSS_YMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_broadcast_ss ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VBROADCASTSS_ZMM_XMM {
    gem5_avx_broadcast_ss zmm, xmmm, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTSS_ZMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_broadcast_ss  zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTSS_ZMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_broadcast_ss zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTSS_XMM_XMM_K {
    gem5_mask_broadcast_ss xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VBROADCASTSS_XMM_M_K {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_mask_broadcast_ss xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VBROADCASTSS_XMM_P_K {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_mask_broadcast_ss xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VBROADCASTSS_YMM_XMM_K {
    gem5_mask_broadcast_ss ymm, xmmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VBROADCASTSS_YMM_M_K {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_mask_broadcast_ss ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VBROADCASTSS_YMM_P_K {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_mask_broadcast_ss ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VBROADCASTSS_ZMM_XMM_K {
    gem5_mask_broadcast_ss zmm, xmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTSS_ZMM_M_K {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_mask_broadcast_ss zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTSS_ZMM_P_K {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_mask_broadcast_ss zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VBROADCASTSD_YMM_XMM {
    gem5_avx_broadcast_sd ymm, xmmm, size=8, ext=YMM
};

def macroop EVEX_VBROADCASTSD_YMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_sd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VBROADCASTSD_YMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_sd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VBROADCASTSD_ZMM_XMM {
    gem5_avx_broadcast_sd zmm, xmmm, size=8, ext=ZMM
};

def macroop EVEX_VBROADCASTSD_ZMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_sd zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VBROADCASTSD_ZMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_sd zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VBROADCASTSD_YMM_XMM_K {
    gem5_mask_broadcast_sd ymm, xmmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VBROADCASTSD_YMM_M_K {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_mask_broadcast_sd ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VBROADCASTSD_YMM_P_K {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_mask_broadcast_sd ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VBROADCASTSD_ZMM_XMM_K {
    gem5_mask_broadcast_sd zmm, xmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VBROADCASTSD_ZMM_M_K {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_mask_broadcast_sd zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VBROADCASTSD_ZMM_P_K {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_mask_broadcast_sd zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VBROADCASTF32X2_YMM_XMM {
    gem5_avx_broadcast_ps ymm, xmmm, size=4, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTF32X2_YMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTF32X2_YMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTF32X2_ZMM_XMM {
    gem5_avx_broadcast_ps zmm, xmmm, size=4, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X2_ZMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X2_ZMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X4_YMM_XMM {
    gem5_avx_broadcast_ps ymm, xmmm, size=4, ext="4 |" + YMM
};

def macroop EVEX_VBROADCASTF32X4_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="4 |" + YMM
};

def macroop EVEX_VBROADCASTF32X4_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_ps ymm, uvec1, size=4, ext="4 |" + YMM
};

def macroop EVEX_VBROADCASTF32X4_ZMM_XMM {
    gem5_avx_broadcast_ps zmm, xmmm, size=4, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X4_ZMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X4_ZMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTF64X2_YMM_XMM {
    gem5_avx_broadcast_pd ymm, xmmm, size=8, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTF64X2_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_pd ymm, uvec1, size=8, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTF64X2_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_pd ymm, uvec1, size=8, ext="2 |" + YMM
};

def macroop EVEX_VBROADCASTF64X2_ZMM_XMM {
    gem5_avx_broadcast_pd zmm, xmmm, size=8, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTF64X2_ZMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTF64X2_ZMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="2 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X8_ZMM_YMM {
    gem5_avx_broadcast_ps zmm, ymmm, size=4, ext="8 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X8_ZMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="8 |" + ZMM
};

def macroop EVEX_VBROADCASTF32X8_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_broadcast_ps zmm, uvec1, size=4, ext="8 |" + ZMM
};

def macroop EVEX_VBROADCASTF64X4_ZMM_YMM {
    gem5_avx_broadcast_pd zmm, ymmm, size=8, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTF64X4_ZMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="4 |" + ZMM
};

def macroop EVEX_VBROADCASTF64X4_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_broadcast_pd zmm, uvec1, size=8, ext="4 |" + ZMM
};

'''
