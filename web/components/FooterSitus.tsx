export function FooterSitus() {
  return (
    <footer className="border-t border-white/5 px-6 py-12">
      <div className="mx-auto max-w-6xl flex flex-col md:flex-row justify-between gap-6 font-mono text-xs text-[#8a8f82]">
        <div>
          <span className="text-[#e8e4dc]">GreenLie</span> | The Orchestra 2026
        </div>
        <div className="flex flex-wrap gap-6">
          <a
            href="https://web-flax-xi-10.vercel.app"
            className="hover:text-[#e8e4dc] transition-colors"
          >
            Live demo
          </a>
          <a
            href="https://github.com/adindamochamad/GreenLie"
            className="hover:text-[#e8e4dc] transition-colors"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </a>
          <a
            href="https://aoagents.dev/"
            className="hover:text-[#e8e4dc] transition-colors"
            target="_blank"
            rel="noopener noreferrer"
          >
            Agent Orchestrator
          </a>
          <span>#agentorchestrator</span>
        </div>
      </div>
    </footer>
  );
}
