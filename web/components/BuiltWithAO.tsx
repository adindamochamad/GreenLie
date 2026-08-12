export function BuiltWithAO() {
  return (
    <section className="border-t border-white/5 px-6 py-24">
      <div className="mx-auto max-w-6xl">
        <div className="grid lg:grid-cols-[1.1fr_1fr] gap-12 items-center">
          <div className="border border-white/10 bg-[#161a14] p-6 font-mono text-xs">
            <div className="text-[#8a8f82] mb-4 border-b border-white/5 pb-2">
              AO Kanban | greenlie project
            </div>
            <div className="space-y-3">
              <div className="flex justify-between text-[#3dff7a]">
                <span>engine/backslide-detector</span>
                <span>Ready to merge</span>
              </div>
              <div className="flex justify-between text-[#ff9500]">
                <span>web/demo-bersebelahan</span>
                <span>In review | 8/12 passed</span>
              </div>
              <div className="flex justify-between text-[#8a8f82]">
                <span>api/fastapi-wrapper</span>
                <span>Working | 2m ago</span>
              </div>
              <div className="flex justify-between text-[#8a8f82]">
                <span>samples/naive-agent-fix</span>
                <span>Working | 14m ago</span>
              </div>
            </div>
            <p className="mt-6 text-[#8a8f82]/60 text-[10px]">
              Replace with real AO Kanban screenshot in demo video
            </p>
          </div>

          <div>
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-[#c44d2e] mb-4">
              Built with AO
            </p>
            <h2
              className="text-3xl tracking-tight mb-4"
              style={{ fontFamily: "var(--font-instrument-serif)" }}
            >
              This repo was built by a fleet
            </h2>
            <p className="text-[#8a8f82] leading-relaxed">
              GreenLie was developed using{" "}
              <a
                href="https://aoagents.dev/"
                className="text-[#e8e4dc] underline underline-offset-4"
                target="_blank"
                rel="noopener noreferrer"
              >
                Agent Orchestrator
              </a>{" "}
              as the workspace - parallel agents on engine, API, and demo site. Demo video
              includes real Kanban footage per hackathon rules.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
