import type { Metadata } from "next";
import { Geist, Geist_Mono, Instrument_Serif } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const instrumentSerif = Instrument_Serif({
  variable: "--font-instrument-serif",
  subsets: ["latin"],
  weight: "400",
  style: ["normal", "italic"],
});

const URL_SITUS = "https://web-flax-xi-10.vercel.app";

export const metadata: Metadata = {
  title: "GreenLie — CI passed. Tests lied.",
  description:
    "Detektor saat agent memperbaiki CI dengan melemahkan test, bukan memperbaiki bug. Built for The Orchestra hackathon.",
  metadataBase: new URL(URL_SITUS),
  openGraph: {
    title: "GreenLie — CI passed. Tests lied.",
    description: "Your Kanban says merge. Your tests say pass. GreenLie catches the lie.",
    url: URL_SITUS,
    siteName: "GreenLie",
    images: [{ url: "/og-image.png", width: 1200, height: 630, alt: "GreenLie" }],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "GreenLie — CI passed. Tests lied.",
    description: "Your Kanban says merge. Your tests say pass. GreenLie catches the lie.",
    images: ["/og-image.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${instrumentSerif.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
