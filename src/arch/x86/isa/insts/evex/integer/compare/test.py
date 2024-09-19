microcode = '''
def macroop EVEX_VPTESTMB_K_XMM_XMM {
    gem5_evex_test_epi8 k, xmm2, xmmm, size=1, ext=XMM
};

def macroop EVEX_VPTESTMB_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi8 k, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPTESTMB_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi8 k, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPTESTMB_K_YMM_YMM {
    gem5_evex_test_epi8 k, ymm2, ymmm, size=1, ext=YMM
};

def macroop EVEX_VPTESTMB_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi8 k, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPTESTMB_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi8 k, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPTESTMB_K_ZMM_ZMM {
    gem5_evex_test_epi8 k, zmm2, zmmm, size=1, ext=ZMM
};

def macroop EVEX_VPTESTMB_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi8 k, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPTESTMB_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi8 k, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPTESTMW_K_XMM_XMM {
    gem5_evex_test_epi16 k, xmm2, xmmm, size=2, ext=XMM
};

def macroop EVEX_VPTESTMW_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi16 k, xmm2, uvec1, size=2, ext=XMM
};

def macroop EVEX_VPTESTMW_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi16 k, xmm2, uvec1, size=2, ext=XMM
};

def macroop EVEX_VPTESTMW_K_YMM_YMM {
    gem5_evex_test_epi16 k, ymm2, ymmm, size=2, ext=YMM
};

def macroop EVEX_VPTESTMW_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi16 k, ymm2, uvec1, size=2, ext=YMM
};

def macroop EVEX_VPTESTMW_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi16 k, ymm2, uvec1, size=2, ext=YMM
};

def macroop EVEX_VPTESTMW_K_ZMM_ZMM {
    gem5_evex_test_epi16 k, zmm2, zmmm, size=2, ext=ZMM
};

def macroop EVEX_VPTESTMW_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi16 k, zmm2, uvec1, size=2, ext=ZMM
};

def macroop EVEX_VPTESTMW_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi16 k, zmm2, uvec1, size=2, ext=ZMM
};

def macroop EVEX_VPTESTMD_K_XMM_XMM {
    gem5_evex_test_epi32 k, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPTESTMD_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPTESTMD_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPTESTMD_K_YMM_YMM {
    gem5_evex_test_epi32 k, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPTESTMD_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPTESTMD_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPTESTMD_K_ZMM_ZMM {
    gem5_evex_test_epi32 k, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPTESTMD_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPTESTMD_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPTESTMQ_K_XMM_XMM {
    gem5_evex_test_epi64 k, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPTESTMQ_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi64 k, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPTESTMQ_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_test_epi64 k, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPTESTMQ_K_YMM_YMM {
    gem5_evex_test_epi64 k, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPTESTMQ_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi64 k, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPTESTMQ_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_test_epi64 k, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPTESTMQ_K_ZMM_ZMM {
    gem5_evex_test_epi64 k, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPTESTMQ_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi64 k, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPTESTMQ_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_test_epi64 k, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPTESTNMB_K_XMM_XMM {
    gem5_evex_testn_epi8 k, xmm2, xmmm, size=1, ext=XMM
};

def macroop EVEX_VPTESTNMB_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi8 k, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPTESTNMB_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi8 k, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPTESTNMB_K_YMM_YMM {
    gem5_evex_testn_epi8 k, ymm2, ymmm, size=1, ext=YMM
};

def macroop EVEX_VPTESTNMB_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi8 k, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPTESTNMB_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi8 k, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPTESTNMB_K_ZMM_ZMM {
    gem5_evex_testn_epi8 k, zmm2, zmmm, size=1, ext=ZMM
};

def macroop EVEX_VPTESTNMB_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi8 k, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPTESTNMB_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi8 k, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPTESTNMW_K_XMM_XMM {
    gem5_evex_testn_epi16 k, xmm2, xmmm, size=2, ext=XMM
};

def macroop EVEX_VPTESTNMW_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi16 k, xmm2, uvec1, size=2, ext=XMM
};

def macroop EVEX_VPTESTNMW_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi16 k, xmm2, uvec1, size=2, ext=XMM
};

def macroop EVEX_VPTESTNMW_K_YMM_YMM {
    gem5_evex_testn_epi16 k, ymm2, ymmm, size=2, ext=YMM
};

def macroop EVEX_VPTESTNMW_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi16 k, ymm2, uvec1, size=2, ext=YMM
};

def macroop EVEX_VPTESTNMW_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi16 k, ymm2, uvec1, size=2, ext=YMM
};

def macroop EVEX_VPTESTNMW_K_ZMM_ZMM {
    gem5_evex_testn_epi16 k, zmm2, zmmm, size=2, ext=ZMM
};

def macroop EVEX_VPTESTNMW_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi16 k, zmm2, uvec1, size=2, ext=ZMM
};

def macroop EVEX_VPTESTNMW_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi16 k, zmm2, uvec1, size=2, ext=ZMM
};

def macroop EVEX_VPTESTNMD_K_XMM_XMM {
    gem5_evex_testn_epi32 k, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPTESTNMD_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPTESTNMD_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi32 k, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPTESTNMD_K_YMM_YMM {
    gem5_evex_testn_epi32 k, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPTESTNMD_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPTESTNMD_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi32 k, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPTESTNMD_K_ZMM_ZMM {
    gem5_evex_testn_epi32 k, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPTESTNMD_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPTESTNMD_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi32 k, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPTESTNMQ_K_XMM_XMM {
    gem5_evex_testn_epi64 k, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPTESTNMQ_K_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi64 k, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPTESTNMQ_K_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_testn_epi64 k, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPTESTNMQ_K_YMM_YMM {
    gem5_evex_testn_epi64 k, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPTESTNMQ_K_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi64 k, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPTESTNMQ_K_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_testn_epi64 k, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPTESTNMQ_K_ZMM_ZMM {
    gem5_evex_testn_epi64 k, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPTESTNMQ_K_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi64 k, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPTESTNMQ_K_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_testn_epi64 k, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPTESTMB_K_XMM_XMM_K {
    gem5_mask_test_epi8 k, xmm2, xmmm, opmask=opmask, size=1, ext=XMM
};

def macroop EVEX_VPTESTMB_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi8 k, xmm2, uvec1, opmask=opmask, size=1, ext=XMM
};

def macroop EVEX_VPTESTMB_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi8 k, xmm2, uvec1, opmask=opmask, size=1, ext=XMM
};

def macroop EVEX_VPTESTMB_K_YMM_YMM_K {
    gem5_mask_test_epi8 k, ymm2, ymmm, opmask=opmask, size=1, ext=YMM
};

def macroop EVEX_VPTESTMB_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi8 k, ymm2, uvec1, opmask=opmask, size=1, ext=YMM
};

def macroop EVEX_VPTESTMB_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi8 k, ymm2, uvec1, opmask=opmask, size=1, ext=YMM
};

def macroop EVEX_VPTESTMB_K_ZMM_ZMM_K {
    gem5_mask_test_epi8 k, zmm2, zmmm, opmask=opmask, size=1, ext=ZMM
};

def macroop EVEX_VPTESTMB_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi8 k, zmm2, uvec1, opmask=opmask, size=1, ext=ZMM
};

def macroop EVEX_VPTESTMB_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi8 k, zmm2, uvec1, opmask=opmask, size=1, ext=ZMM
};

def macroop EVEX_VPTESTMW_K_XMM_XMM_K {
    gem5_mask_test_epi16 k, xmm2, xmmm, opmask=opmask, size=2, ext=XMM
};

def macroop EVEX_VPTESTMW_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi16 k, xmm2, uvec1, opmask=opmask, size=2, ext=XMM
};

def macroop EVEX_VPTESTMW_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi16 k, xmm2, uvec1, opmask=opmask, size=2, ext=XMM
};

def macroop EVEX_VPTESTMW_K_YMM_YMM_K {
    gem5_mask_test_epi16 k, ymm2, ymmm, opmask=opmask, size=2, ext=YMM
};

def macroop EVEX_VPTESTMW_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi16 k, ymm2, uvec1, opmask=opmask, size=2, ext=YMM
};

def macroop EVEX_VPTESTMW_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi16 k, ymm2, uvec1, opmask=opmask, size=2, ext=YMM
};

def macroop EVEX_VPTESTMW_K_ZMM_ZMM_K {
    gem5_mask_test_epi16 k, zmm2, zmmm, opmask=opmask, size=2, ext=ZMM
};

def macroop EVEX_VPTESTMW_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi16 k, zmm2, uvec1, opmask=opmask, size=2, ext=ZMM
};

def macroop EVEX_VPTESTMW_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi16 k, zmm2, uvec1, opmask=opmask, size=2, ext=ZMM
};

def macroop EVEX_VPTESTMD_K_XMM_XMM_K {
    gem5_mask_test_epi32 k, xmm2, xmmm, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPTESTMD_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi32 k, xmm2, uvec1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPTESTMD_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi32 k, xmm2, uvec1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPTESTMD_K_YMM_YMM_K {
    gem5_mask_test_epi32 k, ymm2, ymmm, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPTESTMD_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi32 k, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPTESTMD_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi32 k, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPTESTMD_K_ZMM_ZMM_K {
    gem5_mask_test_epi32 k, zmm2, zmmm, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPTESTMD_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi32 k, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPTESTMD_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi32 k, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPTESTMQ_K_XMM_XMM_K {
    gem5_mask_test_epi64 k, xmm2, xmmm, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPTESTMQ_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi64 k, xmm2, uvec1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPTESTMQ_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_test_epi64 k, xmm2, uvec1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPTESTMQ_K_YMM_YMM_K {
    gem5_mask_test_epi64 k, ymm2, ymmm, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPTESTMQ_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi64 k, ymm2, uvec1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPTESTMQ_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_test_epi64 k, ymm2, uvec1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPTESTMQ_K_ZMM_ZMM_K {
    gem5_mask_test_epi64 k, zmm2, zmmm, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPTESTMQ_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi64 k, zmm2, uvec1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPTESTMQ_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_test_epi64 k, zmm2, uvec1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPTESTNMB_K_XMM_XMM_K {
    gem5_mask_testn_epi8 k, xmm2, xmmm, opmask=opmask, size=1, ext=XMM
};

def macroop EVEX_VPTESTNMB_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi8 k, xmm2, uvec1, opmask=opmask, size=1, ext=XMM
};

def macroop EVEX_VPTESTNMB_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi8 k, xmm2, uvec1, opmask=opmask, size=1, ext=XMM
};

def macroop EVEX_VPTESTNMB_K_YMM_YMM_K {
    gem5_mask_testn_epi8 k, ymm2, ymmm, opmask=opmask, size=1, ext=YMM
};

def macroop EVEX_VPTESTNMB_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi8 k, ymm2, uvec1, opmask=opmask, size=1, ext=YMM
};

def macroop EVEX_VPTESTNMB_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi8 k, ymm2, uvec1, opmask=opmask, size=1, ext=YMM
};

def macroop EVEX_VPTESTNMB_K_ZMM_ZMM_K {
    gem5_mask_testn_epi8 k, zmm2, zmmm, opmask=opmask, size=1, ext=ZMM
};

def macroop EVEX_VPTESTNMB_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi8 k, zmm2, uvec1, opmask=opmask, size=1, ext=ZMM
};

def macroop EVEX_VPTESTNMB_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi8 k, zmm2, uvec1, opmask=opmask, size=1, ext=ZMM
};

def macroop EVEX_VPTESTNMW_K_XMM_XMM_K {
    gem5_mask_testn_epi16 k, xmm2, xmmm, opmask=opmask, size=2, ext=XMM
};

def macroop EVEX_VPTESTNMW_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi16 k, xmm2, uvec1, opmask=opmask, size=2, ext=XMM
};

def macroop EVEX_VPTESTNMW_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi16 k, xmm2, uvec1, opmask=opmask, size=2, ext=XMM
};

def macroop EVEX_VPTESTNMW_K_YMM_YMM_K {
    gem5_mask_testn_epi16 k, ymm2, ymmm, opmask=opmask, size=2, ext=YMM
};

def macroop EVEX_VPTESTNMW_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi16 k, ymm2, uvec1, opmask=opmask, size=2, ext=YMM
};

def macroop EVEX_VPTESTNMW_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi16 k, ymm2, uvec1, opmask=opmask, size=2, ext=YMM
};

def macroop EVEX_VPTESTNMW_K_ZMM_ZMM_K {
    gem5_mask_testn_epi16 k, zmm2, zmmm, opmask=opmask, size=2, ext=ZMM
};

def macroop EVEX_VPTESTNMW_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi16 k, zmm2, uvec1, opmask=opmask, size=2, ext=ZMM
};

def macroop EVEX_VPTESTNMW_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi16 k, zmm2, uvec1, opmask=opmask, size=2, ext=ZMM
};

def macroop EVEX_VPTESTNMD_K_XMM_XMM_K {
    gem5_mask_testn_epi32 k, xmm2, xmmm, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPTESTNMD_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi32 k, xmm2, uvec1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPTESTNMD_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi32 k, xmm2, uvec1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPTESTNMD_K_YMM_YMM_K {
    gem5_mask_testn_epi32 k, ymm2, ymmm, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPTESTNMD_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi32 k, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPTESTNMD_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi32 k, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPTESTNMD_K_ZMM_ZMM_K {
    gem5_mask_testn_epi32 k, zmm2, zmmm, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPTESTNMD_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi32 k, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPTESTNMD_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi32 k, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPTESTNMQ_K_XMM_XMM_K {
    gem5_mask_testn_epi64 k, xmm2, xmmm, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPTESTNMQ_K_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi64 k, xmm2, uvec1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPTESTNMQ_K_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_testn_epi64 k, xmm2, uvec1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPTESTNMQ_K_YMM_YMM_K {
    gem5_mask_testn_epi64 k, ymm2, ymmm, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPTESTNMQ_K_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi64 k, ymm2, uvec1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPTESTNMQ_K_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_testn_epi64 k, ymm2, uvec1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPTESTNMQ_K_ZMM_ZMM_K {
    gem5_mask_testn_epi64 k, zmm2, zmmm, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPTESTNMQ_K_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi64 k, zmm2, uvec1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPTESTNMQ_K_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_testn_epi64 k, zmm2, uvec1, opmask=opmask, size=8, ext=ZMM
};

'''
