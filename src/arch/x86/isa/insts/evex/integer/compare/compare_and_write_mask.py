microcode = '''
def macroop EVEX_VPCMPEQB_K_XMM_XMM {
    gem5_evex_cmpeq_epi8 k, xmm2, xmmm, size=1, ext=XMM
};

def macroop EVEX_VPCMPEQB_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpeq_epi8 k, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPCMPEQB_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpeq_epi8 k, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPCMPEQB_K_YMM_YMM {
    gem5_evex_cmpeq_epi8 k, ymm2, ymmm, size=1, ext=YMM
};

def macroop EVEX_VPCMPEQB_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpeq_epi8 k, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPCMPEQB_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpeq_epi8 k, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPCMPEQB_K_ZMM_ZMM {
    gem5_evex_cmpeq_epi8 k, zmm2, zmmm, size=1, ext=ZMM
};

def macroop EVEX_VPCMPEQB_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpeq_epi8 k, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPCMPEQB_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpeq_epi8 k, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPCMPEQD_K_XMM_XMM {
    gem5_evex_cmpeq_epi32 k, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPCMPEQD_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpeq_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPCMPEQD_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpeq_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPCMPEQD_K_YMM_YMM {
    gem5_evex_cmpeq_epi32 k, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPCMPEQD_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpeq_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPCMPEQD_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpeq_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPCMPEQD_K_ZMM_ZMM {
    gem5_evex_cmpeq_epi32 k, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPCMPEQD_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpeq_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPCMPEQD_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpeq_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPCMPEQD_K_XMM_XMM_K {
    gem5_mask_cmpeq_epi32 k, xmm2, xmmm, k, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPCMPEQD_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_cmpeq_epi32 k, xmm2, uvec1, k, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPCMPEQD_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_cmpeq_epi32 k, xmm2, uvec1, k, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPCMPEQD_K_YMM_YMM_K {
    gem5_mask_cmpeq_epi32 k, ymm2, ymmm, k, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPCMPEQD_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_cmpeq_epi32 k, ymm2, uvec1, k, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPCMPEQD_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_cmpeq_epi32 k, ymm2, uvec1, k, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPCMPEQD_K_ZMM_ZMM_K {
    gem5_mask_cmpeq_epi32 k, zmm2, zmmm, k, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPCMPEQD_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_cmpeq_epi32 k, zmm2, uvec1, k, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPCMPEQD_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_cmpeq_epi32 k, zmm2, uvec1, k, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPCMPGTD_K_XMM_XMM {
    gem5_evex_cmpgt_epi32 k, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPCMPGTD_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpgt_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPCMPGTD_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpgt_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPCMPGTD_K_YMM_YMM {
    gem5_evex_cmpgt_epi32 k, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPCMPGTD_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpgt_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPCMPGTD_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpgt_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPCMPGTD_K_ZMM_ZMM {
    gem5_evex_cmpgt_epi32 k, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPCMPGTD_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpgt_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPCMPGTD_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpgt_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPCMPGTQ_K_XMM_XMM {
    gem5_evex_cmpgt_epi64 k, xmm2, xmmm, destSize=dsz, srcSize=8, ext=XMM
};

def macroop EVEX_VPCMPGTQ_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpgt_epi64 k, xmm2, uvec1, destSize=dsz, srcSize=8, ext=XMM
};

def macroop EVEX_VPCMPGTQ_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmpgt_epi64 k, xmm2, uvec1, destSize=dsz, srcSize=8, ext=XMM
};

def macroop EVEX_VPCMPGTQ_K_YMM_YMM {
    gem5_evex_cmpgt_epi64 k, ymm2, ymmm, destSize=dsz, srcSize=8, ext=YMM
};

def macroop EVEX_VPCMPGTQ_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpgt_epi64 k, ymm2, uvec1, destSize=dsz, srcSize=8, ext=YMM
};

def macroop EVEX_VPCMPGTQ_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmpgt_epi64 k, ymm2, uvec1, destSize=dsz, srcSize=8, ext=YMM
};

def macroop EVEX_VPCMPGTQ_K_ZMM_ZMM {
    gem5_evex_cmpgt_epi64 k, zmm2, zmmm, destSize=dsz, srcSize=8, ext=ZMM
};

def macroop EVEX_VPCMPGTQ_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpgt_epi64 k, zmm2, uvec1, destSize=dsz, srcSize=8, ext=ZMM
};

def macroop EVEX_VPCMPGTQ_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmpgt_epi64 k, zmm2, uvec1, destSize=dsz, srcSize=8, ext=ZMM
};

def macroop EVEX_VPCMPGTD_K_XMM_XMM_K {
    gem5_mask_cmpgt_epi32 k, xmm2, xmmm, k, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPCMPGTD_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_cmpgt_epi32 k, xmm2, uvec1, k, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPCMPGTD_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_cmpgt_epi32 k, xmm2, uvec1, k, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPCMPGTD_K_YMM_YMM_K {
    gem5_mask_cmpgt_epi32 k, ymm2, ymmm, k, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPCMPGTD_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_cmpgt_epi32 k, ymm2, uvec1, k, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPCMPGTD_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_cmpgt_epi32 k, ymm2, uvec1, k, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPCMPGTD_K_ZMM_ZMM_K {
    gem5_mask_cmpgt_epi32 k, zmm2, zmmm, k, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPCMPGTD_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_cmpgt_epi32 k, zmm2, uvec1, k, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPCMPGTD_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_cmpgt_epi32 k, zmm2, uvec1, k, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPCMPD_K_XMM_XMM_I {
    gem5_evex_cmp_epi32 k, xmm2, xmmm, size=4, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPD_K_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epi32 k, xmm2, uvec1, size=4, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPD_K_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epi32 k, xmm2, uvec1, size=4, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPD_K_YMM_YMM_I {
    gem5_evex_cmp_epi32 k, ymm2, ymmm, size=4, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPD_K_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epi32 k, ymm2, uvec1, size=4, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPD_K_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epi32 k, ymm2, uvec1, size=4, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPD_K_ZMM_ZMM_I {
    gem5_evex_cmp_epi32 k, zmm2, zmmm, size=4, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPD_K_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epi32 k, zmm2, uvec1, size=4, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPD_K_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epi32 k, zmm2, uvec1, size=4, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPQ_K_XMM_XMM_I {
    gem5_evex_cmp_epi64 k, xmm2, xmmm, size=8, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPQ_K_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epi64 k, xmm2, uvec1, size=8, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPQ_K_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epi64 k, xmm2, uvec1, size=8, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPQ_K_YMM_YMM_I {
    gem5_evex_cmp_epi64 k, ymm2, ymmm, size=8, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPQ_K_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epi64 k, ymm2, uvec1, size=8, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPQ_K_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epi64 k, ymm2, uvec1, size=8, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPQ_K_ZMM_ZMM_I {
    gem5_evex_cmp_epi64 k, zmm2, zmmm, size=8, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPQ_K_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epi64 k, zmm2, uvec1, size=8, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPQ_K_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epi64 k, zmm2, uvec1, size=8, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPUD_K_XMM_XMM_I {
    gem5_evex_cmp_epu32 k, xmm2, xmmm, size=4, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPUD_K_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epu32 k, xmm2, uvec1, size=4, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPUD_K_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epu32 k, xmm2, uvec1, size=4, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPUD_K_YMM_YMM_I {
    gem5_evex_cmp_epu32 k, ymm2, ymmm, size=4, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPUD_K_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epu32 k, ymm2, uvec1, size=4, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPUD_K_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epu32 k, ymm2, uvec1, size=4, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPUD_K_ZMM_ZMM_I {
    gem5_evex_cmp_epu32 k, zmm2, zmmm, size=4, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPUD_K_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epu32 k, zmm2, uvec1, size=4, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPUD_K_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epu32 k, zmm2, uvec1, size=4, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPUQ_K_XMM_XMM_I {
    gem5_evex_cmp_epu64 k, xmm2, xmmm, size=8, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPUQ_K_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epu64 k, xmm2, uvec1, size=8, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPUQ_K_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_epu64 k, xmm2, uvec1, size=8, ext="IMMEDIATE |" + XMM
};

def macroop EVEX_VPCMPUQ_K_YMM_YMM_I {
    gem5_evex_cmp_epu64 k, ymm2, ymmm, size=8, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPUQ_K_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epu64 k, ymm2, uvec1, size=8, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPUQ_K_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_epu64 k, ymm2, uvec1, size=8, ext="IMMEDIATE |" + YMM
};

def macroop EVEX_VPCMPUQ_K_ZMM_ZMM_I {
    gem5_evex_cmp_epu64 k, zmm2, zmmm, size=8, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPUQ_K_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epu64 k, zmm2, uvec1, size=8, ext="IMMEDIATE |" + ZMM
};

def macroop EVEX_VPCMPUQ_K_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_epu64 k, zmm2, uvec1, size=8, ext="IMMEDIATE |" + ZMM
};

'''
