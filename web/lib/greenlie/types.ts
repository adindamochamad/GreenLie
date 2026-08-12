export interface Assertion {
  teks: string;
  baris: number;
  tingkat_ketat: number;
  jenis: string;
}

export interface TemuanBackslide {
  id: string;
  severity: string;
  sebelum: string;
  sesudah: string;
  alasan: string;
  berkas: string;
  baris: number;
  confidence: number;
}

export interface LaporanIntegritas {
  integrity_score: number;
  temuan: TemuanBackslide[];
  assertion_dicek: number;
  assertion_aman: number;
  metode: string;
  berkas_test: string[];
}

export interface LaporanAnalisisResponse extends LaporanIntegritas {
  duration_ms: number;
}
