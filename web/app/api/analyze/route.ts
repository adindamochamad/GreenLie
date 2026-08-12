import { NextResponse } from "next/server";
import { jalankanAnalisis } from "@/lib/greenlie/layanan";

export async function POST(request: Request) {
  try {
    const body = (await request.json()) as { sample?: string };
    const idSample = body.sample ?? "naive-agent";
    const laporan = jalankanAnalisis(idSample);
    return NextResponse.json(laporan);
  } catch (err) {
    const pesan = err instanceof Error ? err.message : "Analisis gagal";
    const status = pesan.includes("tidak dikenal") ? 400 : 500;
    return NextResponse.json({ detail: pesan }, { status });
  }
}
