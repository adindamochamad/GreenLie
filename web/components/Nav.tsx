import Link from "next/link";

export function Nav() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 border-b border-white/5 bg-[#0d0f0c]/80 backdrop-blur-md">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Link href="/" className="font-mono text-sm tracking-tight text-[#e8e4dc]">
          Green<span className="text-[#3dff7a]">Lie</span>
        </Link>
        <nav className="flex items-center gap-6 text-sm text-[#8a8f82]">
          <a href="#demo" className="hover:text-[#e8e4dc] transition-colors">
            Demo
          </a>
          <a
            href="https://github.com/adindamochamad/GreenLie"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-[#e8e4dc] transition-colors"
          >
            GitHub
          </a>
          <a
            href="#try"
            className="border border-[#c44d2e]/60 px-3 py-1.5 text-[#e8e4dc] hover:bg-[#c44d2e]/10 transition-colors"
          >
            Run scan
          </a>
        </nav>
      </div>
    </header>
  );
}
