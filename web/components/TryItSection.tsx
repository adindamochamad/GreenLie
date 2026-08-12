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

const URL_API = process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "");

async function ambilLaporan(): Promise<{ laporan: Laporan; sumber: "api" | "cache" }> {
  if (URL_API) {
    try {
      const res = await fetch(`${URL_API}/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sample: "naive-agent" }),
      });
      if (res.ok) {
        return { laporan: await res.json(), sumber: "api" };
      }
    } catch {
      // Fallback ke golden report jika API belum siap
    }
  }

  const res = await fetch("/golden-report.json");
  if (!res.ok) throw new Error("golden-report tidak ditemukan");
  return { laporan: await res.json(), sumber: "cache" };
}

export function TryItSection() {
  const [memuat, setMemuat] = useState(false);
  const [laporan, setLaporan] = useState<Laporan | null>(null);
  const [sumber, setSumber] = useState<"api" | "cache" | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function jalankanScan() {
    setMemuat(true);
    setLaporan(null);
    setError(null);
    setSumber(null);

    try {
      const { laporan: data, sumber: asal } = await ambilLaporan();
      setLaporan(data);
      setSumber(asal);
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
            {URL_API ? " Calls live API when available." : ""}
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
              <div className="text-[#ff3b30] text-lg font-bold">
                Integrity: {laporan.integrity_score}% | {laporan.temuan.length} findings
              </div>
              <p className="text-[#8a8f82] text-xs">
                {laporan.assertion_aman}/{laporan.assertion_dicek} assertions intact
                {sumber === "api" && laporan.duration_ms != null
                  ? ` · ${laporan.duration_ms}ms via API`
                  : sumber === "cache"
                    ? " · cached engine output"
                    : ""}
              </p>
              <ul className="space-y-2 text-xs max-h-48 overflow-y-auto">
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
