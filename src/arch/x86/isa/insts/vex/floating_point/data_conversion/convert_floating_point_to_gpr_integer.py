microcode = '''
def macroop VEX_VCVTSS2SI_R_XMM {
    sse_cvtf2i_vec2fp ufp1, xmmm, srcSize=4, destSize=dsz, ext = Scalar + "| 4"
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTSS2SI_R_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=4, destSize=dsz, ext = Scalar + "| 4"
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTSS2SI_R_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=4, destSize=dsz, ext = Scalar + "| 4"
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTSD2SI_R_XMM {
    sse_cvtf2i_vec2fp ufp1, xmmm, srcSize=8, destSize=dsz, ext = Scalar + "| 4"
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTSD2SI_R_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=8, destSize=dsz, ext = Scalar + "| 4"
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTSD2SI_R_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=8, destSize=dsz, ext = Scalar + "| 4"
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTTSS2SI_R_XMM {
    sse_cvtf2i_vec2fp ufp1, xmmm, srcSize=4, destSize=dsz, ext=Scalar
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTTSS2SI_R_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=4, destSize=dsz, ext=Scalar
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTTSS2SI_R_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=4, destSize=dsz, ext=Scalar
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTTSD2SI_R_XMM {
    sse_cvtf2i_vec2fp ufp1, xmmm, srcSize=8, destSize=dsz, ext=Scalar
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTTSD2SI_R_M {
    ldfp ufp1, seg, sib, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=8, destSize=dsz, ext=Scalar
    mov2int reg, ufp1, size=dsz
};

def macroop VEX_VCVTTSD2SI_R_P {
    rdip t7
    ldfp ufp1, seg, riprel, disp, dataSize=8
    cvtf2i ufp1, ufp1, srcSize=8, destSize=dsz, ext=Scalar
    mov2int reg, ufp1, size=dsz
};
'''
