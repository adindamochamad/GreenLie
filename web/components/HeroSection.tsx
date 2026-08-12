export function HeroSection() {
  return (
    <section className="relative min-h-[92vh] flex flex-col justify-end pb-16 pt-32 px-6 overflow-hidden">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_-10%,rgba(61,255,122,0.07),transparent)]" />

      <div className="relative mx-auto max-w-6xl w-full">
        <div className="mb-8 inline-flex items-center gap-2 border border-[#3dff7a]/30 bg-[#3dff7a]/5 px-3 py-1 font-mono text-xs text-[#3dff7a] badge-fake-green">
          CI PASS | 44/44 tests
        </div>

        <h1
          className="font-[family-name:var(--font-instrument-serif)] text-[clamp(2.75rem,8vw,5.5rem)] leading-[0.95] tracking-tight max-w-4xl"
          style={{ fontFamily: "var(--font-instrument-serif)" }}
        >
          Your board says{" "}
          <em className="text-[#3dff7a] not-italic">merge.</em>
          <br />
          Your tests say{" "}
          <em className="text-[#8a8f82] not-italic">pass.</em>
          <br />
          <span className="text-[#ff3b30]">Production says outage.</span>
        </h1>

        <p className="mt-8 max-w-xl text-lg text-[#8a8f82] leading-relaxed">
          GreenLie catches when your agent &quot;fixes&quot; CI by weakening{" "}
          <code className="font-mono text-[#e8e4dc]">expect(status).toBe(401)</code> into{" "}
          <code className="font-mono text-[#ff9500]">toBeGreaterThan(0)</code> - before
          it ships.
        </p>

        <div className="mt-10 flex flex-wrap gap-4">
          <a
            href="#demo"
            className="bg-[#c44d2e] px-6 py-3 font-mono text-sm text-[#e8e4dc] hover:bg-[#a84326] transition-colors"
          >
            See the green lie
          </a>
          <a
            href="https://aoagents.dev/"
            target="_blank"
            rel="noopener noreferrer"
            className="border border-white/10 px-6 py-3 font-mono text-sm text-[#8a8f82] hover:border-white/20 hover:text-[#e8e4dc] transition-colors"
          >
            Built with AO
          </a>
        </div>
      </div>
    </section>
  );
}
