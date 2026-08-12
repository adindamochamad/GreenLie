const LANGKAH = [
  {
    nomor: "01",
    judul: "Diff test files",
    deskripsi: "Compare before/after agent fix across *.test.js, *.spec.ts, test_*.py",
  },
  {
    nomor: "02",
    judul: "Parse assertions",
    deskripsi: "Score strictness: toBe(401) = 90, toBeGreaterThan(0) = 50, toBeDefined = 30",
  },
  {
    nomor: "03",
    judul: "Verdict",
    deskripsi: "Flag TEST_BACKSLIDE and ASSERTION_DROPPED before merge",
  },
];

export function HowItWorks() {
  return (
    <section className="border-t border-white/5 px-6 py-24 bg-[#161a14]/50">
      <div className="mx-auto max-w-6xl">
        <p className="font-mono text-xs uppercase tracking-[0.2em] text-[#c44d2e] mb-4">
          Mechanism
        </p>
        <h2
          className="text-3xl md:text-4xl tracking-tight mb-16 max-w-lg"
          style={{ fontFamily: "var(--font-instrument-serif)" }}
        >
          How GreenLie reads a PR
        </h2>

        <div className="grid md:grid-cols-3 gap-px bg-white/5">
          {LANGKAH.map((item) => (
            <div key={item.nomor} className="bg-[#0d0f0c] p-8">
              <span className="font-mono text-4xl text-[#c44d2e]/40">{item.nomor}</span>
              <h3 className="mt-4 font-mono text-lg text-[#e8e4dc]">{item.judul}</h3>
              <p className="mt-3 text-sm text-[#8a8f82] leading-relaxed">{item.deskripsi}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
