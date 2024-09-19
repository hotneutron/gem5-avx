microcode = '''
def macroop EVEX_VMOVD_XMM_R {
    gem5_mm256_move_epi32_si128 xmm, regm, srcSize=dsz, destSize=8
};

def macroop EVEX_VMOVD_XMM_M {
    ldvec256lo64 xmm, seg, sib, disp, dataSize=dsz
};

def macroop EVEX_VMOVD_XMM_P {
    rdip t7
    ldvec256lo64 xmm, seg, riprel, disp, dataSize=dsz
};

def macroop EVEX_VMOVD_R_XMM {
    gem5_mm256_move_si128_epi32 reg, xmmm, size=dsz
};

def macroop EVEX_VMOVD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=dsz
};

def macroop EVEX_VMOVD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=dsz
};

def macroop EVEX_VMOVQ_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=Scalar
};

def macroop EVEX_VMOVQ_XMM_R {
   gem5_mm256_move_epi64_si128 xmm, regm, srcSize=8, destSize=8
};

def macroop EVEX_VMOVQ_XMM_M {
    ldvec256lo64 xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVQ_XMM_P {
    rdip t7
    ldvec256lo64 xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVQ_R_XMM {
    gem5_mm256_move_si128_epi64 reg, xmmm, size=8
};

def macroop EVEX_VMOVQ_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVQ_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVDQA32_XMM_XMM {
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQA32_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA32_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA32_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA32_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA32_YMM_YMM {
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQA32_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA32_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA32_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA32_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA32_ZMM_ZMM {
    gem5_avx_move_epu32 zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQA32_ZMM_M {
    ldvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA32_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA32_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA32_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA64_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQA64_XMM_M {
    ldvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop EVEX_VMOVDQA64_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VMOVDQA64_M_XMM {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop EVEX_VMOVDQA64_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VMOVDQA64_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQA64_YMM_M {
    ldvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop EVEX_VMOVDQA64_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VMOVDQA64_M_YMM {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop EVEX_VMOVDQA64_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VMOVDQA64_ZMM_ZMM {
    gem5_avx_move_epu64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQA64_ZMM_M {
    ldvec512 zmm, seg, sib, disp, dataSize=64
};

def macroop EVEX_VMOVDQA64_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, disp, dataSize=64
};

def macroop EVEX_VMOVDQA64_M_ZMM {
    stvec512 zmm, seg, sib, disp, dataSize=64
};

def macroop EVEX_VMOVDQA64_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, disp, dataSize=64
};

def macroop EVEX_VMOVDQU_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQU_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQU_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};
 
def macroop EVEX_VMOVDQU32_XMM_XMM {
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQU32_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU32_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU32_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU32_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU32_YMM_YMM {
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQU32_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU32_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU32_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU32_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU32_ZMM_ZMM {
    gem5_avx_move_epu32 zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQU32_ZMM_M {
    ldvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU32_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU32_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU32_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU64_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQU64_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU64_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU64_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU64_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU64_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQU64_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU64_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU64_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU64_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU64_ZMM_ZMM {
    gem5_avx_move_epu64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQU64_ZMM_M {
    ldvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU64_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU64_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU64_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA32_XMM_XMM_K {
    gem5_mask_move_epu32 xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQA32_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQA32_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQA32_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA32_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA32_YMM_YMM_K {
    gem5_mask_move_epu32 ymm, ymmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQA32_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQA32_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQA32_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA32_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA32_ZMM_ZMM_K {
    gem5_mask_move_epu32 zmm, zmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQA32_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQA32_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQA32_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA32_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU32_XMM_XMM_K {
    gem5_mask_move_epu32 xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQU32_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQU32_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVDQU32_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU32_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU32_YMM_YMM_K {
    gem5_mask_move_epu32 ymm, ymmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQU32_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQU32_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVDQU32_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU32_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU32_ZMM_ZMM_K {
    gem5_mask_move_epu32 zmm, zmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQU32_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQU32_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVDQU32_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU32_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA64_XMM_XMM_K {
    gem5_mask_move_epu64 xmm, xmmm, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQA64_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQA64_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQA64_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA64_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQA64_YMM_YMM_K {
    gem5_mask_move_epu64 ymm, ymmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQA64_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQA64_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQA64_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA64_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQA64_ZMM_ZMM_K {
    gem5_mask_move_epu64 zmm, zmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQA64_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQA64_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQA64_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQA64_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU64_XMM_XMM_K {
    gem5_mask_move_epu64 xmm, xmmm, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQU64_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQU64_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDQU64_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU64_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVDQU64_YMM_YMM_K {
    gem5_mask_move_epu64 ymm, ymmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQU64_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQU64_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVDQU64_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU64_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVDQU64_ZMM_ZMM_K {
    gem5_mask_move_epu64 zmm, zmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQU64_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQU64_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDQU64_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVDQU64_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VPCOMPRESSD_XMM_XMM {
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPCOMPRESSD_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPCOMPRESSD_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPCOMPRESSD_YMM_YMM {
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPCOMPRESSD_YMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_YMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VPCOMPRESSD_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VPCOMPRESSD_ZMM_ZMM {
    gem5_avx_move_epu32 zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPCOMPRESSD_ZMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_ZMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VPCOMPRESSD_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VPCOMPRESSQ_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPCOMPRESSQ_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_M_XMM {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop EVEX_VPCOMPRESSQ_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VPCOMPRESSQ_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPCOMPRESSQ_YMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_YMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_M_YMM {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop EVEX_VPCOMPRESSQ_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VPCOMPRESSQ_ZMM_ZMM {
    gem5_avx_move_epu64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPCOMPRESSQ_ZMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_ZMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_M_ZMM {
    stvec512 zmm, seg, sib, disp, dataSize=64
};

def macroop EVEX_VPCOMPRESSQ_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, disp, dataSize=64
};

def macroop EVEX_VPCOMPRESSD_XMM_XMM_K {
    gem5_mask_compress_epi32 xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VPCOMPRESSD_XMM_M_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_XMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_M_XMM_K {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPCOMPRESSD_P_XMM_K {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VPCOMPRESSD_YMM_YMM_K {
    gem5_mask_compress_epi32 ymm, ymmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VPCOMPRESSD_YMM_M_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_YMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_M_YMM_K {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VPCOMPRESSD_P_YMM_K {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VPCOMPRESSD_ZMM_ZMM_K {
    gem5_mask_compress_epi32 zmm, zmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VPCOMPRESSD_ZMM_M_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_ZMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSD_M_ZMM_K {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VPCOMPRESSD_P_ZMM_K {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VPCOMPRESSQ_XMM_XMM_K {
    gem5_mask_compress_epi64 xmm, xmmm, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VPCOMPRESSQ_XMM_M_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_XMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_M_XMM_K {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop EVEX_VPCOMPRESSQ_P_XMM_K {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VPCOMPRESSQ_YMM_YMM_K {
    gem5_mask_compress_epi64 ymm, ymmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VPCOMPRESSQ_YMM_M_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_YMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_M_YMM_K {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop EVEX_VPCOMPRESSQ_P_YMM_K {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VPCOMPRESSQ_ZMM_ZMM_K {
    gem5_mask_compress_epi64 zmm, zmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VPCOMPRESSQ_ZMM_M_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_ZMM_P_K {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPCOMPRESSQ_M_ZMM_K {
    stvec512 zmm, seg, sib, disp, dataSize=64
};

def macroop EVEX_VPCOMPRESSQ_P_ZMM_K {
    rdip t7
    stvec512 zmm, seg, riprel, disp, dataSize=64
};

'''
