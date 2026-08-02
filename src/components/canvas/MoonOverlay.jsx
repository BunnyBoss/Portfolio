import { Suspense } from "react";
import { Canvas } from "@react-three/fiber";
import { useScroll, useTransform } from "framer-motion";
import { motion } from "framer-motion-3d";
import { useTexture, Float } from "@react-three/drei";

const MoonMesh = () => {
  const moonTexture = useTexture('/moon_1024.jpg');

  // Track global window scroll
  const { scrollYProgress } = useScroll();

  // Position X: 
  // 0 -> Center (Hero)
  // 0.2 -> 0.85 -> Middle Right (Sidebar)
  // 0.85 -> 1.0 -> Center Right (Contact Section)
  const xPos = useTransform(scrollYProgress, [0, 0.2, 0.85, 1.3], [0, 2.9, 2.9, 1.2]);

  // Scale: 
  // 0 -> 1.2 (Hero)
  // 0.2 -> 0.85 -> 0.35 (Sidebar)
  // 0.85 -> 1.0 -> 1.4 (Huge crescent in Contact)
  const scale = useTransform(scrollYProgress, [0, 0.2, 0.85, 1], [1.2, 0.35, 0.35, 1.0]);

  // Lighting: directional light position to create true crescent
  // By moving Z from +12 (front) to -12 (back) linearly, it crosses 0 at exactly 50% scroll.
  // This guarantees a perfectly smooth Full -> Half -> Crescent transition across the entire page.
  const lightX = useTransform(scrollYProgress, [0, 1], [0, -10]);
  const lightY = useTransform(scrollYProgress, [0, 1], [2, -10]);
  const lightZ = useTransform(scrollYProgress, [0, 1], [12, -20]);

  // Increase intensity heavily as it goes behind to keep the sliver bright
  const lightIntensity = useTransform(scrollYProgress, [0, 1], [1.5, 30]);

  // Rotate moon as we scroll (180 degree rotation from the classic face)
  const moonRotationY = useTransform(scrollYProgress, [0, 1], [-Math.PI / 2, (-Math.PI / 2) + Math.PI]);

  return (
    <>
      <ambientLight intensity={0.01} />
      {/* Dynamic light creating the phases of the moon */}
      <motion.directionalLight
        intensity={lightIntensity}
        color="#ffffff"
        position-x={lightX}
        position-y={lightY}
        position-z={lightZ}
      />
      {/* Subtle neon rim light for the cyberpunk aesthetic */}
      <directionalLight
        intensity={0.1}
        color="#A8C4D4"
        position={[5, -5, -5]}
      />

      <Float speed={1.5} rotationIntensity={0.2} floatIntensity={0.5}>
        <motion.mesh
          scale={scale}
          position-x={xPos}
          rotation-y={moonRotationY}
        >
          <sphereGeometry args={[1, 64, 64]} />
          <meshStandardMaterial
            map={moonTexture}
            emissive="#ffffff"
            emissiveIntensity={0.01} // Even darker emissive for more realistic shadows
            roughness={1}
          />
        </motion.mesh>
      </Float>
    </>
  );
};

const MoonOverlayCanvas = () => {
  return (
    <div className="w-full h-screen fixed inset-0 z-[-1] pointer-events-none">
      <Canvas
        camera={{ position: [0, 0, 5], fov: 45 }}
        gl={{ preserveDrawingBuffer: true, alpha: true }}
      >
        <Suspense fallback={null}>
          <MoonMesh />
        </Suspense>
      </Canvas>
    </div>
  );
};

export default MoonOverlayCanvas;
