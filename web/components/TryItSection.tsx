"use client";

import { useState } from "react";

interface Temuan {
  id: string;
  severity: string;
  sebelum: string;
  sesudah: string;
  alasan: string;
}

interface Laporan {
  integrity_score: number;
  assertion_dicek: number;
  assertion_aman: number;
  temuan: Temuan[];
  duration_ms?: number;
}

async function ambilLaporan(): Promise<Laporan> {
  const res = await fetch("/api/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sample: "naive-agent" }),
  });

  if (!res.ok) {
    throw new Error("API analyze gagal");
  }

  return res.json();
}

export function TryItSection() {
  const [memuat, setMemuat] = useState(false);
  const [laporan, setLaporan] = useState<Laporan | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function jalankanScan() {
    setMemuat(true);
    setLaporan(null);
    setError(null);

    try {
      const data = await ambilLaporan();
      setLaporan(data);
    } catch {
      setError("Scan gagal — jalankan ./scripts/demo.sh secara lokal");
    } finally {
      setMemuat(false);
    }
  }

  return (
    <section id="try" className="border-t border-white/5 px-6 py-24">
      <div className="mx-auto max-w-6xl grid lg:grid-cols-2 gap-12 items-start">
        <div>
          <p className="font-mono text-xs uppercase tracking-[0.2em] text-[#c44d2e] mb-4">
            Try it
          </p>
          <h2
            className="text-3xl tracking-tight mb-4"
            style={{ fontFamily: "var(--font-instrument-serif)" }}
          >
            Run on the sample agent fix
          </h2>
          <p className="text-[#8a8f82] mb-6">
            Pre-baked scenario: auth tests weakened by a naive CI-fix agent.
            Live scan via <code className="text-[#e8e4dc]">POST /api/analyze</code>.
          </p>
          <button
            type="button"
            onClick={jalankanScan}
            disabled={memuat}
            className="bg-[#c44d2e] px-6 py-3 font-mono text-sm disabled:opacity-50 hover:bg-[#a84326] transition-colors"
          >
            {memuat ? "Scanning..." : "greenlie analyze"}
          </button>
        </div>

        <div className="border border-white/10 bg-[#1c2118] p-6 font-mono text-sm min-h-[200px]">
          {memuat && (
            <div className="text-[#8a8f82] animate-pulse">Parsing assertions...</div>
          )}
          {error && <div className="text-[#ff3b30]">{error}</div>}
          {laporan && (
            <div className="space-y-4">
              <div className="flex flex-wrap items-center gap-2">
                <span className="inline-block bg-[#ff3b30]/15 border border-[#ff3b30]/40 px-2 py-0.5 text-[10px] uppercase tracking-wider text-[#ff3b30]">
                  Merge blocked
                </span>
                {laporan.duration_ms != null && (
                  <span className="inline-block bg-[#3dff7a]/10 border border-[#3dff7a]/30 px-2 py-0.5 text-[10px] uppercase tracking-wider text-[#3dff7a]">
                    Live scan · {laporan.duration_ms}ms
                  </span>
                )}
              </div>
              <div className="text-[#ff3b30] text-lg font-bold">
                Integrity: {laporan.integrity_score}% | {laporan.temuan.length} findings
              </div>
              <p className="text-[#8a8f82] text-xs">
                {laporan.assertion_aman}/{laporan.assertion_dicek} assertions intact
              </p>
              {laporan.temuan[0] && (
                <div className="border border-white/10 bg-[#161a14] p-3 text-xs space-y-2">
                  <p className="text-[#ff3b30] font-bold">{laporan.temuan[0].id} · {laporan.temuan[0].severity}</p>
                  <p>
                    <span className="text-[#8a8f82]">Before:</span>{" "}
                    <span className="text-[#e8e4dc]">{laporan.temuan[0].sebelum}</span>
                  </p>
                  <p>
                    <span className="text-[#8a8f82]">After:</span>{" "}
                    <span className="text-[#ff3b30]">{laporan.temuan[0].sesudah}</span>
                  </p>
                </div>
              )}
              <ul className="space-y-2 text-xs max-h-36 overflow-y-auto">
                {laporan.temuan.map((t) => (
                  <li key={t.id} className="border-l-2 border-[#ff3b30] pl-3 text-[#8a8f82]">
                    <span className="text-[#ff3b30]">{t.id}</span>{" "}
                    {t.alasan.split(" - ")[0]}
                  </li>
                ))}
              </ul>
            </div>
          )}
          {!memuat && !laporan && !error && (
            <div className="text-[#8a8f82]/50">Output appears here</div>
          )}
        </div>
      </div>
    </section>
  );
}
