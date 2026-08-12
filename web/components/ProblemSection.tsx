export function ProblemSection() {
  return (
    <section className="border-t border-white/5 px-6 py-24">
      <div className="mx-auto max-w-6xl grid lg:grid-cols-[1fr_1.2fr] gap-16 items-start">
        <div>
          <p className="font-mono text-xs uppercase tracking-[0.2em] text-[#c44d2e] mb-4">
            The failure mode
          </p>
          <h2
            className="text-3xl md:text-4xl leading-tight tracking-tight"
            style={{ fontFamily: "var(--font-instrument-serif)" }}
          >
            What happens when the model is working, confident, and wrong?
          </h2>
        </div>

        <div className="space-y-6 text-[#8a8f82] leading-relaxed">
          <p>
            Agent Orchestrator routes CI failures back to the agent that wrote the code.
            That loop is powerful - until the agent edits the test instead of the bug.
          </p>
          <p>
            Most tools check <strong className="text-[#e8e4dc]">does it break?</strong>{" "}
            GreenLie checks{" "}
            <strong className="text-[#ff3b30]">did the test get weaker?</strong>
          </p>
          <ul className="font-mono text-sm space-y-2 border-l-2 border-[#ff3b30]/40 pl-4">
            <li className="text-[#ff3b30]">TEST_BACKSLIDE - exact to range</li>
            <li className="text-[#ff9500]">TEST_BACKSLIDE - string to toBeDefined()</li>
            <li className="text-[#ff3b30]">ASSERTION_DROPPED - agent deleted the check</li>
          </ul>
        </div>
      </div>
    </section>
  );
}
