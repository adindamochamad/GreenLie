import { readFileSync } from "fs";
import { join } from "path";
import { analisisSample, kumpulkanBerkasSample } from "./detector";
import type { LaporanAnalisisResponse } from "./types";

const SAMPLE_TERDAFTAR: Record<string, string> = {
  "naive-agent": "naive-agent",
};

function bacaSample(idSample: string): Map<string, { sebelum: string; sesudah: string }> {
  const namaFolder = SAMPLE_TERDAFTAR[idSample];
  if (!namaFolder) {
    throw new Error(`Sample tidak dikenal: ${idSample}`);
  }

  const akarSample = join(process.cwd(), "data", "samples", namaFolder);
  const relBerkas = "tests/auth.test.js";
  const sebelum = readFileSync(join(akarSample, "before", relBerkas), "utf-8");
  const sesudah = readFileSync(join(akarSample, "after", relBerkas), "utf-8");

  return new Map([[relBerkas, { sebelum, sesudah }]]);
}

export function jalankanAnalisis(idSample: string): LaporanAnalisisResponse {
  const mulai = performance.now();
  const berkasMap = bacaSample(idSample);
  const berkasList = kumpulkanBerkasSample(berkasMap);
  const laporan = analisisSample(berkasList);
  const durasiMs = Math.round(performance.now() - mulai);

  return {
    ...laporan,
    duration_ms: durasiMs,
  };
}

export const VERSI_API = "0.1.0";
