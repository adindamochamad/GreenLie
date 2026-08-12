"use client";

import { useEffect, useState } from "react";

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
}

const KODE_SEBELUM = `expect(response.status).toBe(401);
expect(response.body.error).toBe('Unauthorized');
expect(response.body.user.id).toBe('user-123');`;

const KODE_SESUDAH = `expect(response.status).toBeGreaterThan(0);
expect(response.body.error).toBeDefined();
// user.id assertion deleted`;

export function DemoBersebelahan() {
  const [laporan, setLaporan] = useState<Laporan | null>(null);
  const [fase, setFase] = useState<"naive" | "greenlie">("naive");

  useEffect(() => {
    fetch("/golden-report.json")
      .then((r) => r.json())
      .then(setLaporan)
      .catch(() => null);
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      setFase((f) => (f === "naive" ? "greenlie" : "naive"));
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  const skor = laporan?.integrity_score ?? 29;

  return (
    <section id="demo" className="border-t border-white/5 px-6 py-24 demo-cursor-crosshair">
      <div className="mx-auto max-w-6xl">
        <div className="mb-12 flex flex-col md:flex-row md:items-end md:justify-between gap-6">
          <div>
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-[#c44d2e] mb-4">
              Side-by-side
            </p>
            <h2
              className="text-3xl md:text-4xl tracking-tight"
              style={{ fontFamily: "var(--font-instrument-serif)" }}
            >
              Same agent fix. Two outcomes.
            </h2>
          </div>
          <div className="flex gap-2 font-mono text-xs">
            <button
              type="button"
              onClick={() => setFase("naive")}
              className={`px-3 py-1.5 border transition-colors ${
                fase === "naive"
                  ? "border-[#3dff7a]/50 bg-[#3dff7a]/10 text-[#3dff7a]"
                  : "border-white/10 text-[#8a8f82]"
              }`}
            >
              Naive merge
            </button>
            <button
              type="button"
              onClick={() => setFase("greenlie")}
              className={`px-3 py-1.5 border transition-colors ${
                fase === "greenlie"
                  ? "border-[#ff3b30]/50 bg-[#ff3b30]/10 text-[#ff3b30]"
                  : "border-white/10 text-[#8a8f82]"
              }`}
            >
              GreenLie block
            </button>
          </div>
        </div>

        <div className="grid lg:grid-cols-2 gap-4">
          {/* Panel kiri: diff test */}
          <div className="relative scan-line border border-white/10 bg-[#161a14] overflow-hidden">
            <div className="border-b border-white/5 px-4 py-2 font-mono text-xs text-[#8a8f82] flex justify-between">
              <span>tests/auth.test.js</span>
              <span className="text-[#ff9500]">agent fix diff</span>
            </div>
            <div className="grid grid-cols-2 divide-x divide-white/5 font-mono text-xs leading-6">
              <pre className="p-4 text-[#8a8f82] overflow-x-auto">
                <span className="block text-[#8a8f82]/60 mb-2">before</span>
                {KODE_SEBELUM.split("\n").map((baris) => (
                  <div key={baris} className="text-[#e8e4dc]">
                    {baris}
                  </div>
                ))}
              </pre>
              <pre className="p-4 overflow-x-auto">
                <span className="block text-[#8a8f82]/60 mb-2">after</span>
                {KODE_SESUDAH.split("\n").map((baris) => (
                  <div
                    key={baris}
                    className={
                      baris.includes("toBeGreaterThan") || baris.includes("toBeDefined")
                        ? "text-[#ff9500]"
                        : baris.startsWith("//")
                          ? "text-[#ff3b30] line-through"
                          : "text-[#e8e4dc]"
                    }
                  >
                    {baris}
                  </div>
                ))}
              </pre>
            </div>
          </div>

          {/* Panel kanan: outcome */}
          <div
            className={`border p-6 transition-all duration-500 ${
              fase === "naive"
                ? "border-[#3dff7a]/30 bg-[#3dff7a]/5"
                : "border-[#ff3b30]/30 bg-[#ff3b30]/5"
            }`}
          >
            {fase === "naive" ? (
              <div className="space-y-4">
                <div className="badge-fake-green inline-block font-mono text-sm text-[#3dff7a] border border-[#3dff7a]/40 px-3 py-1">
                  AO Kanban: Ready to merge
                </div>
                <p className="text-[#8a8f82]">
                  CI passes. Board green. Nobody noticed the test stopped checking 401.
                </p>
                <p className="font-mono text-xs text-[#3dff7a]">
                  44/44 tests passed | PR #327 approved
                </p>
              </div>
            ) : (
              <div className="space-y-4">
                <div className="font-mono text-5xl font-bold text-[#ff3b30] tabular-nums">
                  {skor}%
                  <span className="block text-xs font-normal text-[#8a8f82] mt-1">
                    integrity score
                  </span>
                </div>
                <p className="text-[#e8e4dc]">
                  {laporan?.temuan.length ?? 5} findings blocked merge.
                </p>
                <ul className="space-y-2 font-mono text-xs max-h-52 overflow-y-auto">
                  {(laporan?.temuan ?? []).map((t) => (
                    <li key={t.id} className="border-l-2 border-[#ff3b30] pl-3 text-[#8a8f82]">
                      <span className="text-[#ff3b30]">{t.id}</span>{" "}
                      {t.alasan.split(" - ")[0]}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
