microcode = '''
def macroop VEX_VPCMPEQB_XMM_XMM_XMM {
    gem5_avx_cmpeq_epu8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop VEX_VPCMPEQB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpeq_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPCMPEQB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpeq_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPCMPEQB_YMM_YMM_YMM {
    gem5_avx_cmpeq_epu8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop VEX_VPCMPEQB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpeq_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPCMPEQB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpeq_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPCMPEQD_XMM_XMM_XMM {
    gem5_avx_cmpeq_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPCMPEQD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpeq_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPCMPEQD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpeq_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPCMPEQD_YMM_YMM_YMM {
    gem5_avx_cmpeq_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPCMPEQD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpeq_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPCMPEQD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpeq_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPCMPEQQ_XMM_XMM_XMM {
    gem5_avx_cmpeq_epu64 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPCMPEQQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpeq_epu64 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPCMPEQQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpeq_epu64 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPCMPEQQ_YMM_YMM_YMM {
    gem5_avx_cmpeq_epu64 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPCMPEQQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpeq_epu64 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPCMPEQQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpeq_epu64 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPCMPGTB_XMM_XMM_XMM {
    gem5_avx_cmpgt_epi8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop VEX_VPCMPGTB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpgt_epi8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPCMPGTB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpgt_epi8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPCMPGTQ_XMM_XMM_XMM {
    gem5_avx_cmpgt_epi64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VPCMPGTQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpgt_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPCMPGTQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpgt_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPCMPGTQ_YMM_YMM_YMM {
    gem5_avx_cmpgt_epi64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VPCMPGTQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpgt_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPCMPGTQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpgt_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPCMPGTQ_ZMM_ZMM_ZMM {
    gem5_avx_cmpgt_epi64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop VEX_VPCMPGTQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_cmpgt_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop VEX_VPCMPGTQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_cmpgt_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop VEX_VPCMPGTB_YMM_YMM_YMM {
    gem5_avx_cmpgt_epi8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop VEX_VPCMPGTB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpgt_epi8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPCMPGTB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpgt_epi8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPCMPGTD_XMM_XMM_XMM {
    gem5_avx_cmpgt_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPCMPGTD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpgt_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPCMPGTD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmpgt_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPCMPGTD_YMM_YMM_YMM {
    gem5_avx_cmpgt_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPCMPGTD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpgt_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPCMPGTD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmpgt_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

'''
