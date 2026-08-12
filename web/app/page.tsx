import { BuiltWithAO } from "@/components/BuiltWithAO";
import { DemoBersebelahan } from "@/components/DemoBersebelahan";
import { FooterSitus } from "@/components/FooterSitus";
import { HeroSection } from "@/components/HeroSection";
import { HowItWorks } from "@/components/HowItWorks";
import { Nav } from "@/components/Nav";
import { ProblemSection } from "@/components/ProblemSection";
import { TryItSection } from "@/components/TryItSection";

export default function HomePage() {
  return (
    <>
      <Nav />
      <main>
        <HeroSection />
        <ProblemSection />
        <DemoBersebelahan />
        <HowItWorks />
        <TryItSection />
        <BuiltWithAO />
      </main>
      <FooterSitus />
    </>
  );
}
