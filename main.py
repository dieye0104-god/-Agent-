import os
from agents.observer import ObserverAgent
from agents.refactor import RefactorAgent
from agents.validator import ValidatorAgent

def run_migration_pipeline(source_code):
    print("🚀 开始多 Agent 协同重构任务...")
    
    # 1. 感知阶段
    observer = ObserverAgent()
    analysis = observer.analyze(source_code)
    print(f"✅ [Observer] 识别到旧版 API 引用点: {len(analysis['deprecated_points'])} 处")

    # 2. 重构阶段 (长链推理)
    refactor = RefactorAgent()
    new_code = refactor.generate(source_code, analysis)
    print("✅ [Refactor] 新版代码重写完成")

    # 3. 验证阶段 (闭环修复)
    validator = ValidatorAgent()
    is_valid, report = validator.verify(new_code)
    
    if is_valid:
        print("🎉 [Validator] 验证通过！代码已就绪。")
        return new_code
    else:
        print(f"❌ [Validator] 发现错误: {report}. 正在触发自愈流...")
        # 此处可扩展重新重构的逻辑
        return None

if __name__ == "__main__":
    # 模拟 Expo AV 的旧代码
    legacy_code = "import { Audio } from 'expo-av'; const playback = new Audio.Sound();"
    result = run_migration_pipeline(legacy_code)