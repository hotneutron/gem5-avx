uint64_t tcomp(int size, uint64_t comp, uint64_t arg1, uint64_t arg2)
{
	uint64_t result = 0;
	for(int i=0; i<size; i++)
		result |= ((comp >> i) & mask(1)) ?
			((arg1 >> i) & mask(1)) : ((arg2 >> i) & mask(1));
	return result;
}

uint64_t vpternlog_table(uint8_t idx, int size, uint64_t A, uint64_t B, uint64_t C)
{
    uint64_t result = 0, temp1, temp2;
    int i;
    switch(idx) {
    case 0x00: result = 0; break;
    case 0x01: result = ~(A | B | C); break;
    case 0x02: result = C & ~(A | B); break;
    case 0x03: result = ~(A | B); break;
    case 0x04: result = B & ~(A | C); break;
    case 0x05: result = ~(C | A); break;
    case 0x06: result = ~(A | ~(B ^ C)); break;
    case 0x07: result = ~(A | (B & C)); break;
    case 0x08: result = ~(A | ~(B & C)); break;
    case 0x09: result = ~(A | (B ^ C)); break;
    case 0x0A: result = ~A & C; break;
    case 0x0B: result = tcomp(size, C, ~A, ~(A | B)); break;
    case 0x0C: result = ~A & B; break;
    case 0x0D: result = tcomp(size, B, ~A, ~(A | C)); break;
    case 0x0E: result = ~(A | ~(B | C)); break;
    case 0x0F: result = ~A; break;

    case 0x10: result = A & ~(B | C); break;
    case 0x11: result = ~(B | C); break;
    case 0x12: result = ~(B | ~(A ^ C)); break;
    case 0x13: result = ~(B | (A & C)); break;
    case 0x14: result = ~(C | ~(A ^ B)); break;
    case 0x15: result = ~(C | (A & B)); break;
    case 0x16: result = tcomp(size, A, ~(B | C), B ^ C); break;
    case 0x17:
		result = ( B < C ) ? B : C;
		if( result > A ) result = A;
		break;
    case 0x18: result = tcomp(size, A, ~(B | C), B & C); break;
    case 0x19: result = tcomp(size, A, ~(B | C), ~(B ^ C)); break;
    case 0x1A: result = tcomp(size, A, ~(B | C), C); break;
    case 0x1B: result = tcomp(size, C, ~A, ~B); break;
    case 0x1C: result = tcomp(size, A, ~(B | C), B); break;
    case 0x1D: result = tcomp(size, B, ~A, ~C); break;
    case 0x1E: result = (A ^ (B | C)); break;
    case 0x1F: result = ~(A & (B | C)); break;

    case 0x20: result = ~(B | ~(A & C)); break;
    case 0x21: result = ~(B | (A ^ C)); break;
    case 0x22: result = ~B & C; break;
    case 0x23: result = tcomp(size, C, ~B, ~(A | B)); break;
    case 0x24: result = tcomp(size, B, ~(A | C), A & C); break;
    case 0x25: result = tcomp(size, B, ~(A | C), ~(A ^ C)); break;
    case 0x26: result = tcomp(size, B, ~(A | C), C); break;
    case 0x27: result = tcomp(size, C, ~B, ~A); break;
    case 0x28: result = C & (A ^ B); break;
    case 0x29: result = tcomp(size, C, A ^ B, ~(A | B)); break;
    case 0x2A: result = C & ~(A & B); break;
    case 0x2B: result = tcomp(size, C, ~(A & B), ~(A | B)); break;
    case 0x2C: result = tcomp(size, B, ~A, A & C); break;
    case 0x2D: result = tcomp(size, B, ~A, ~(A ^ C)); break;
    case 0x2E: result = tcomp(size, B, ~A, C); break;
    case 0x2F: result = tcomp(size, C, ~(A & B), ~A); break;

    case 0x30: result = A & ~B; break;
    case 0x31: result = tcomp(size, A, ~B, ~(B | C)); break;
    case 0x32: result = ~(B | ~(A | C)); break;
    case 0x33: result = ~B; break;
    case 0x34: result = tcomp(size, B, ~(A | C), A); break;
    case 0x35: result = tcomp(size, A, ~B, ~C); break;
    case 0x36: result = B ^ (A | C); break;
    case 0x37: result = ~(B & (A | C)); break;
    case 0x38: result = tcomp(size, A, ~B, B & C); break;
    case 0x39: result = tcomp(size, A, ~B, ~(B ^ C)); break;
    case 0x3A: result = tcomp(size, A, ~B, C); break;
    case 0x3B: result = tcomp(size, C, ~(A & B), ~B); break;
    case 0x3C: result = A ^ B; break;
    case 0x3D: result = tcomp(size, C, A ^ B, ~(A & B)); break;
    case 0x3E: result = tcomp(size, A, ~B, B | C); break;
    case 0x3F: result = ~(A & B); break;

    case 0x40: result = ~(C | ~(A & B)); break;
    case 0x41: result = ~(C | (A ^ B)); break;
    case 0x42: result = tcomp(size, C, ~(A | B), A & B); break;
    case 0x43: result = tcomp(size, C, ~(A | B), A ^ B); break;
    case 0x44: result = B & ~C; break;
    case 0x45: result = tcomp(size, B, ~C, ~(A | C)); break;
    case 0x46: result = tcomp(size, C, ~(A | B), B); break;
    case 0x47: result = tcomp(size, B, ~C, ~A); break;
    case 0x48: result = B & (A ^ C); break;
    case 0x49: result = tcomp(size, B, A ^ C, ~(A | C)); break;
    case 0x4A: result = tcomp(size, C, ~A, A & B); break;
    case 0x4B: result = tcomp(size, B, A ^ C, ~A); break;
    case 0x4C: result = B & ~(A & C); break;
    case 0x4D: result = tcomp(size, B, ~(A & C), ~(A | C)); break;
    case 0x4E: result = tcomp(size, C, ~A, B); break;
    case 0x4F: result = tcomp(size, B, ~(A & C), ~A); break;

    case 0x50: result = A & ~C; break;
    case 0x51: result = tcomp(size, A, ~C, ~(B & C)); break;
    case 0x52: result = tcomp(size, C, ~(A | B), A); break;
    case 0x53: result = tcomp(size, A, ~C, ~B); break;
    case 0x54: result = ~(C | ~(A | B)); break;
    case 0x55: result = ~C; break;
    case 0x56: result = C ^ (A | B); break;
    case 0x57: result = ~(C & (A | B)); break;
    case 0x58: result = tcomp(size, A, ~C, B & C); break;
    case 0x59: result = tcomp(size, A, ~C, ~(B ^ C)); break;
    case 0x5A: result = C ^ A; break;
    case 0x5B: result = tcomp(size, B, A ^ C, ~(A & C)); break;
    case 0x5C: result = tcomp(size, A, ~C, B); break;
    case 0x5D: result = tcomp(size, B, ~(A & C), ~C); break;
    case 0x5E: result = tcomp(size, A, ~C, B | C); break;
    case 0x5F: result = ~(A & C); break;

    case 0x60: result = A & (B ^ C); break;
    case 0x61: result = tcomp(size, A, B ^ C, ~(B | C)); break;
    case 0x62: result = tcomp(size, C, ~B, A & B); break;
    case 0x63: result = tcomp(size, A, B ^ C, ~B); break;
    case 0x64: result = tcomp(size, B, ~C, A & C); break;
    case 0x65: result = tcomp(size, A, B ^ C, ~C); break;
    case 0x66: result = B ^ C; break;
    case 0x67: result = tcomp(size, A, B ^ C, ~(B & C)); break;
    case 0x68: result = tcomp(size, A, B ^ C, B & C); break;
    case 0x69: result = ~(A ^ B ^ C); break;
    case 0x6A: result = C ^ (A & B); break;
    case 0x6B: result = tcomp(size, C, ~(A & B), ~(A ^ B)); break;
    case 0x6C: result = B ^ (A & C); break;
    case 0x6D: result = tcomp(size, B, ~(A & C), ~(A ^ C)); break;
    case 0x6E: result = tcomp(size, B, ~(A & C), C); break;
    case 0x6F: result = ~(A & ~(B ^ C)); break;

    case 0x70: result = A & ~(B & C); break;
    case 0x71: result = tcomp(size, A, ~(B & C), ~(B | C)); break;
    case 0x72: result = tcomp(size, C, ~B, A); break;
    case 0x73: result = tcomp(size, A, ~(B & C), ~B); break;
    case 0x74: result = tcomp(size, B, ~C, A); break;
    case 0x75: result = tcomp(size, A, ~(B & C), ~C); break;
    case 0x76: result = tcomp(size, B, ~C, A | C); break;
    case 0x77: result = ~(B & C); break;
    case 0x78: result = A & (B & C); break;
    case 0x79: result = tcomp(size, A, ~(B & C), ~(B ^ C)); break;
    case 0x7A: result = tcomp(size, A, ~(B & C), C); break;
    case 0x7B: result = ~(B & ~(A ^ C)); break;
    case 0x7C: result = tcomp(size, A, ~(B & C), B); break;
    case 0x7D: result = ~(C & ~(A ^ B)); break;
    case 0x7E: result = tcomp(size, A, ~(B & C), B | C); break;
    case 0x7F: result = ~(A & B & C); break;

    case 0x80: result = A & B & C; break;
    case 0x81: result = tcomp(size, A, B & C, ~(B | C)); break;
    case 0x82: result = C & ~(A ^ B); break;
    case 0x83: result = tcomp(size, A, B & C, ~B); break;
    case 0x84: result = B & ~(A ^ C); break;
    case 0x85: result = tcomp(size, A, B & C, ~C); break;
    case 0x86: result = tcomp(size, A, B & C, B ^ C); break;
    case 0x87: result = ~(A ^ (B & C)); break;
    case 0x88: result = B & C; break;
    case 0x89: result = tcomp(size, B, C, ~(A | C)); break;
    case 0x8A: result = tcomp(size, A, B & C, C); break;
    case 0x8B: result = tcomp(size, B, C, ~A); break;
    case 0x8C: result = tcomp(size, A, B & C, B); break;
    case 0x8D: result = tcomp(size, C, B, ~A); break;
    case 0x8E: result = tcomp(size, A, B & C, B | C); break;
    case 0x8F: result = ~(A & ~(B & C)); break;

    case 0x90: result = A & ~(B ^ C); break;
    case 0x91: result = tcomp(size, B, A & C, ~C); break;
    case 0x92: result = tcomp(size, C, ~B, A & B); break;
    case 0x93: result = ~(B & (A & C)); break;
    case 0x94: result = tcomp(size, C, A & B, A ^ B); break;
    case 0x95: result = ~(C ^ (A & B)); break;
    case 0x96: result = A ^ B ^ C; break;
    case 0x97: result = tcomp(size, A, ~(B ^ C), ~(B & C)); break;
    case 0x98: result = tcomp(size, A, ~(B ^ C), B & C); break;
    case 0x99: result = ~(C ^ B); break;
    case 0x9A: result = tcomp(size, A, ~(B ^ C), C); break;
    case 0x9B: result = tcomp(size, B, C, ~(A & C)); break;
    case 0x9C: result = tcomp(size, A, ~(B ^ C), B); break;
    case 0x9D: result = tcomp(size, C, B, ~(A & B)); break;
    case 0x9E: result = tcomp(size, A, ~(B ^ C), B | C); break;
    case 0x9F: result = ~(A & (B ^ C)); break;

    case 0xA0: result = A & C; break;
    case 0xA1: result = tcomp(size, A, C, ~(B | C)); break;
    case 0xA2: result = tcomp(size, B, A & C, C); break;
    case 0xA3: result = tcomp(size, A, C, ~B); break;
    case 0xA4: result = tcomp(size, B, ~(A ^ C), A & C); break;
    case 0xA5: result = ~(C ^ A); break;
    case 0xA6: result = tcomp(size, A, C, B ^ C); break;
    case 0xA7: result = tcomp(size, A, C, ~(B & C)); break;
    case 0xA8: result = C & (A | B); break;
    case 0xA9: result = ~(C ^ (A | B)); break;
    case 0xAA: result = C; break;
    case 0xAB: result = C | ~(A | B); break;
    case 0xAC: result = tcomp(size, A, C, B); break;
    case 0xAD: result = tcomp(size, C, A | B, ~A); break;
    case 0xAE: result = tcomp(size, A, C, B | C); break;
    case 0xAF: result = C | ~A; break;

    case 0xB0: result = tcomp(size, B, A & C, A); break;
    case 0xB1: result = tcomp(size, C, A, ~B); break;
    case 0xB2: result = tcomp(size, B, A & C, A | C); break;
    case 0xB3: result = ~(B & ~(A & C)); break;
    case 0xB4: result = tcomp(size, B, ~(A ^ C), A); break;
    case 0xB5: result = tcomp(size, C, A, ~(A & B)); break;
    case 0xB6: result = tcomp(size, B, ~(A ^ C), A | C); break;
    case 0xB7: result = ~(B & (A ^ C)); break;
    case 0xB8: result = tcomp(size, B, C, A); break;
    case 0xB9: result = tcomp(size, C, A | B, ~B); break;
    case 0xBA: result = tcomp(size, B, C, A | C); break;
    case 0xBB: result = C | ~B; break;
    case 0xBC: result = tcomp(size, C, A | B, A ^ B); break;
    case 0xBD: result = tcomp(size, C, A | B, ~(A & B)); break;
    case 0xBE: result = C | (B ^ A); break;
    case 0xBF: result = C | ~(A & B); break;

    case 0xC0: result = A & B; break;
    case 0xC1: result = tcomp(size, A, B, ~(B | C)); break;
    case 0xC2: result = tcomp(size, C, ~(A ^ B), A & B); break;
    case 0xC3: result = ~(A ^ B); break;
    case 0xC4: result = tcomp(size, C, A & B, B); break;
    case 0xC5: result = tcomp(size, A, B, ~C); break;
    case 0xC6: result = tcomp(size, A, B, B ^ C); break;
    case 0xC7: result = tcomp(size, A, B, ~(B & C)); break;
    case 0xC8: result = B & (A | C); break;
    case 0xC9: result = ~(B ^ (A | C)); break;
    case 0xCA: result = tcomp(size, A, B, C); break;
    case 0xCB: result = tcomp(size, B, A | C, ~A); break;
    case 0xCC: result = B; break;
    case 0xCD: result = B | ~(A | C); break;
    case 0xCE: result = tcomp(size, A, B, B | C); break;
    case 0xCF: result = B | ~A; break;

    case 0xD0: result = tcomp(size, C, A & B, A); break;
    case 0xD1: result = tcomp(size, B, A, ~C); break;
    case 0xD2: result = tcomp(size, B, A, A ^ C); break;
    case 0xD3: result = tcomp(size, B, A, ~(A & C)); break;
    case 0xD4: result = tcomp(size, C, A & B, A | B); break;
    case 0xD5: result = ~(C & ~(A & B)); break;
    case 0xD6: result = tcomp(size, C, ~(A ^ B), A | B); break;
    case 0xD7: result = ~(C & (A ^ B)); break;
    case 0xD8: result = tcomp(size, C, B, A); break;
    case 0xD9: result = tcomp(size, B, A | C, ~C); break;
    case 0xDA: result = tcomp(size, B, A | C, A ^ C); break;
    case 0xDB: result = tcomp(size, B, A | C, ~(A & C)); break;
    case 0xDC: result = tcomp(size, C, B, A | B); break;
    case 0xDD: result = B | ~C; break;
    case 0xDE: result = B | (A ^ C); break;
    case 0xDF: result = B | ~(A & C); break;

    case 0xE0: result = A & (B | C); break;
    case 0xE1: result = ~(A ^ (B | C)); break;
    case 0xE2: result = tcomp(size, B, A, C); break;
    case 0xE3: result = tcomp(size, A, B | C, ~B); break;
    case 0xE4: result = tcomp(size, C, A, B); break;
    case 0xE5: result = tcomp(size, A, B | C, ~C); break;
    case 0xE6: result = tcomp(size, A, B | C, B ^ C); break;
    case 0xE7: result = tcomp(size, A, B | C, ~(B & C)); break;
    case 0xE8:
		result = ( B > C ) ? B : C;
		if( result < A ) result = A;
		break;
    case 0xE9: result = tcomp(size, A, B | C, ~(B ^ C)); break;
    case 0xEA: result = C | (A & B); break;
    case 0xEB: result = C | ~(A ^ B); break;
    case 0xEC: result = B | (A & C); break;
    case 0xED: result = B | ~(A ^ C); break;
    case 0xEE: result = B | C; break;
    case 0xEF: result = ~(A & ~(B | C)); break;

    case 0xF0: result = A; break;
    case 0xF1: result = A | ~(B | C); break;
    case 0xF2: result = tcomp(size, B, A, A | C); break;
    case 0xF3: result = A | ~B; break;
    case 0xF4: result = tcomp(size, C, A, A | B); break;
    case 0xF5: result = A | ~C; break;
    case 0xF6: result = A | (B ^ C); break;
    case 0xF7: result = A | ~(B & C); break;
    case 0xF8: result = A | (B & C); break;
    case 0xF9: result = A | ~(B ^ C); break;
    case 0xFA: result = A | C; break;
    case 0xFB: result = ~(B & ~(A | C)); break;
    case 0xFC: result = A | B; break;
    case 0xFD: result = ~(C & ~(A | B)); break;
    case 0xFE: result = A | B | C; break;
    case 0xFF: result = mask(size); break;
    }

	return result & mask(size);
}

